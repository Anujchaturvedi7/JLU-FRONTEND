<template>
  <div class="weapon-detection-page">
    <h1>Weapon Detection</h1>

    <!-- Button to start live detection -->
    <button @click="startWeaponDetection" class="btn">Detect Weapon Live</button>

    <!-- Display video stream and status -->
    <div v-if="isMonitoring" class="monitoring-container">
      <video ref="video" id="video" autoplay playsinline width="100%" height="auto"></video>
      <div class="status">
        <p>Status: {{ detectionStatus }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isMonitoring: false,
      detectionStatus: "Waiting for detection...",
      videoStream: null,
    };
  },
  methods: {
    async startWeaponDetection() {
      try {
        // Access the webcam
        const stream = await navigator.mediaDevices.getUserMedia({
          video: true
        });
        this.$refs.video.srcObject = stream; // Bind webcam stream to the video element
        this.videoStream = stream;
        this.isMonitoring = true;
        this.detectionStatus = "Detecting...";

        // Start capturing frames and sending them to backend for detection
        this.captureFrames();
      } catch (error) {
        console.error("Error accessing webcam: ", error);
        alert("Could not access the webcam.");
      }
    },

    async captureFrames() {
      const videoElement = this.$refs.video;

      // Capture frames from video feed every 100ms (or adjust as needed)
      const captureInterval = setInterval(async () => {
        if (this.isMonitoring) {
          const frame = this.captureFrame(videoElement);
          await this.detectWeapon(frame); // Send frame to backend for detection
        } else {
          clearInterval(captureInterval); // Stop capturing when monitoring is stopped
        }
      }, 100);
    },

    captureFrame(videoElement) {
      // Create a canvas to capture a frame from the video
      const canvas = document.createElement("canvas");
      canvas.width = videoElement.videoWidth;
      canvas.height = videoElement.videoHeight;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
      return canvas.toDataURL("image/jpeg"); // Return the captured frame as base64 image
    },

    async detectWeapon(frame) {
      try {
        const response = await fetch('http://your-backend-api-url/detect_weapon', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ image: frame }) // Send frame as base64 image
        });

        const result = await response.json();

        // Update status based on detection result
        if (result.weaponDetected) {
          this.detectionStatus = "Weapon Detected!";
        } else {
          this.detectionStatus = "No Weapon Detected.";
        }
      } catch (error) {
        console.error("Error detecting weapon:", error);
        this.detectionStatus = "Error in detection.";
      }
    },

    stopMonitoring() {
      if (this.videoStream) {
        this.videoStream.getTracks().forEach(track => track.stop());
      }
      this.isMonitoring = false;
      this.detectionStatus = "Monitoring Stopped.";
    }
  }
};
</script>

<style scoped>
.weapon-detection-page {
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  color: #ffffff;
  padding: 30px;
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 50px;
  color: #00bcd4;
  text-shadow: 0 0 10px #00bcd4;
}

.btn {
  padding: 12px 30px;
  font-size: 1rem;
  background-color: #00bcd4;
  color: white;
  text-decoration: none;
  border-radius: 10px;
  transition: background-color 0.3s;
  margin: 10px;
  box-shadow: 0 4px 10px rgba(0, 188, 212, 0.4);
}

.btn:hover {
  background-color: #0097a7;
  box-shadow: 0 6px 15px rgba(0, 188, 212, 0.6);
}

.monitoring-container {
  margin-top: 20px;
}

video {
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 188, 212, 0.5);
}

.status {
  margin-top: 20px;
  font-size: 1.2rem;
  color: #00bcd4;
  text-shadow: 0 0 5px #00bcd4;
}
</style>
