<template>
  <div class="dashboard-container">
    <button class="logout-button" @click="logout">Logout</button>

    <h1 class="glow-text welcome-text">👋 Welcome, User!</h1>

    <!-- Upload Form -->
    <form @submit.prevent="handleSubmit" class="upload-form">
      <div class="form-group">
        <label class="glow-text">Missing Person's Name:</label>
        <input type="text" v-model="personName" placeholder="Enter name" required />
      </div>

      <div class="form-group">
        <label class="glow-text">Upload Photo:</label>
        <input type="file" @change="handleFileChange" accept="image/*" required />
      </div>

      <button type="submit">Upload</button>
    </form>

    <!-- Success Popup -->
    <div v-if="showPopup" class="popup">
      ✅ Complaint filed successfully!
    </div>
  </div>
</template>

<script>
export default {
  name: "UserDashboard",
  data() {
    return {
      personName: "",
      selectedFile: null,
      showPopup: false,
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async handleSubmit() {
      if (!this.personName || !this.selectedFile) return;

      const formData = new FormData();
      formData.append("name", this.personName);
      formData.append("photo", this.selectedFile);

      try {
        const response = await fetch("http://localhost:8000/upload-missing-person", {
          method: "POST",
          body: formData,
        });

        const result = await response.json();
        if (response.ok) {
          this.showPopup = true;
          setTimeout(() => {
            this.showPopup = false;
          }, 2000);
          this.personName = "";
          this.selectedFile = null;
        } else {
          alert("Upload failed: " + result.detail);
        }
      } catch (err) {
        console.error(err);
        alert("Something went wrong!");
      }
    },
    logout() {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
/* Top-right logout button in red neon */
.logout-button {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background-color: transparent;
  color: #ff4c4c;
  border: 2px solid #ff4c4c;
  padding: 0.5rem 1rem;
  font-weight: bold;
  border-radius: 10px;
  cursor: pointer;
  transition: 0.3s;
  box-shadow: 0 0 10px #ff4c4c88;
}
.logout-button:hover {
  background-color: #ff4c4c;
  color: black;
  box-shadow: 0 0 20px #ff4c4c;
}

/* Fullscreen dark neon background */
.dashboard-container {
  height: 100vh;
  width: 100%;
  padding: 2rem;
  background: linear-gradient(145deg, #0d0d1f, #0a0a1a);
  color: #00ffee;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  overflow-x: hidden;
  box-sizing: border-box;
}

/* Welcome text */
.welcome-text {
  font-size: 3rem;
  margin: 0 0 7rem; /* Increased the gap below the welcome text */
  text-shadow: 0 0 8px #00ffee, 0 0 20px #00ffee55;
  text-align: center;
}

/* Form group with aligned labels and inputs */
.form-group {
  display: flex;
  align-items: center;
  gap: 1.5rem;  /* Increased gap between label and input */
  margin: 1.5rem 0; /* Added more space between fields */
  width: 100%;
  max-width: 550px;
}

.form-group label {
  min-width: 180px;
  text-align: left;
  font-size: 1.1rem;
}

/* Upload form styling */
.upload-form {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 550px;
  gap: 2rem;  /* Add more space between each form group */
  align-items: stretch;
}

/* Neon label text */
.glow-text {
  font-weight: bold;
  color: #00ffee;
  text-shadow: 0 0 8px #00ffee, 0 0 5px #00ffee88;
}

/* Input fields styling */
input[type="text"],
input[type="file"] {
  padding: 0.8rem;
  background-color: #1a1a2e;
  border: 2px solid #00ffee;
  color: white;
  border-radius: 12px;
  box-shadow: 0 0 8px #00ffee33;
  outline: none;
  font-size: 1rem;
  width: 100%;  /* Make inputs take full available width */
}
input[type="file"]{
  border-radius: 30px;
}
/* Submit button styling */
button[type="submit"] {
  background-color: #00ffee;
  color: #000;
  padding: 0.8rem;
  font-size: 1.1rem;
  border: none;
  border-radius: 12px;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 0 5px #00ffeeaa;
  transition: 0.3s;
}

button[type="submit"]:hover {
  background-color: #00e6d0;
  box-shadow: 0 0 10px #00ffeecc;
}

/* Success popup */
.popup {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #00ffee;
  color: black;
  border-radius: 10px;
  text-align: center;
  font-weight: bold;
  box-shadow: 0 0 20px #00ffee99;
  animation: fadeInOut 2s ease-in-out;
}

@keyframes fadeInOut {
  0% { opacity: 0; transform: scale(0.9); }
  10% { opacity: 1; transform: scale(1); }
  90% { opacity: 1; transform: scale(1); }
  100% { opacity: 0; transform: scale(0.95); }
}
</style>
