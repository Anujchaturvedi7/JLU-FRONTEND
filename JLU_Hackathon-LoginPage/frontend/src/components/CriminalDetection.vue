<template>
  <div class="criminal-detection-page">
    <h1>Criminal Detection</h1>

    <button @click="startMonitoring" class="btn">Start Monitoring</button>

    <div v-if="monitoring" class="video-container">
      <video ref="video" autoplay playsinline width="100%" height="auto"></video>
      <p class="status">Status: {{ status }}</p>
    </div>

    <div v-if="criminalDetected" class="report-card">
      <h2>🚨 Criminal Detected</h2>
      <div class="report-images">
        <div>
          <h3>Dataset Photo</h3>
          <img :src="detectedInfo.datasetImage" alt="Dataset" />
        </div>
        <div>
          <h3>Live Capture</h3>
          <img :src="detectedInfo.liveCapture" alt="Live" />
        </div>
      </div>
      <p><strong>Name:</strong> {{ detectedInfo.name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      monitoring: false,
      status: "Idle",
      videoStream: null,
      criminalDetected: false,
      detectedInfo: {
        name: '',
        datasetImage: '',
        liveCapture: ''
      }
    };
  },
  methods: {
    async startMonitoring() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        this.$refs.video.srcObject = stream;
        this.videoStream = stream;
        this.monitoring = true;
        this.status = "Monitoring for criminals...";
        this.captureLoop();
      } catch (err) {
        console.error("Camera access failed", err);
        this.status = "Camera access failed";
      }
    },

    async captureLoop() {
      const video = this.$refs.video;
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');

      const loop = async () => {
        if (!this.monitoring) return;
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        const frame = canvas.toDataURL('image/jpeg');

        const response = await fetch("http://your-backend-api-url/detect_criminal", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ image: frame })
        });

        const result = await response.json();

        if (result.detected) {
          this.status = "Criminal Found!";
          this.criminalDetected = true;
          this.detectedInfo = {
            name: result.name,
            datasetImage: result.dataset_image, // URL from backend
            liveCapture: frame // Live frame at detection time
          };
          this.stopMonitoring();
        } else {
          this.status = "Scanning...";
          setTimeout(loop, 500); // Continue after delay
        }
      };

      loop();
    },

    stopMonitoring() {
      this.monitoring = false;
      if (this.videoStream) {
        this.videoStream.getTracks().forEach(track => track.stop());
      }
    }
  }
};
</script>

<style scoped>
.criminal-detection-page {
  background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
  color: #ffffff;
  padding: 30px;
  text-align: center;
  font-family: 'Segoe UI', sans-serif;
}

h1 {
  font-size: 2.8rem;
  margin-bottom: 30px;
  color: #00bcd4;
  text-shadow: 0 0 8px #00bcd4;
}

.btn {
  padding: 14px 36px;
  font-size: 1.2rem;
  background-color: #00bcd4;
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: 0.3s;
  box-shadow: 0 4px 12px rgba(0, 188, 212, 0.3);
}

.btn:hover {
  background-color: #0097a7;
  box-shadow: 0 6px 18px rgba(0, 188, 212, 0.5);
}

.video-container {
  margin-top: 25px;
}

video {
  max-width: 640px;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0, 188, 212, 0.4);
}

.status {
  margin-top: 10px;
  font-size: 1.2rem;
  color: #00bcd4;
}

.report-card {
  background: #112;
  border: 1px solid #00bcd4;
  margin: 30px auto;
  padding: 20px;
  max-width: 720px;
  border-radius: 16px;
  box-shadow: 0 0 20px rgba(0, 188, 212, 0.4);
}

.report-images {
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
}

.report-images img {
  width: 240px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 188, 212, 0.3);
}

.report-card h2 {
  color: #ff5252;
  text-shadow: 0 0 8px #ff1744;
}
</style>
