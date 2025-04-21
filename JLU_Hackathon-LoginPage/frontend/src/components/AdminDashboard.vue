<template>
  <div class="dashboard">
    <h1>Welcome, Admin!</h1>

    <div class="card-container">
      <div class="card-block" @click="goTo('MissingPerson')">
        <div class="card">
          <img src="/missing-person.webp" class="card-image" alt="Missing Person" />
        </div>
        <p class="label">Missing Person</p>
      </div>
      <div class="card-block" @click="goTo('WeaponDetection')">
        <div class="card">
          <img src="/weapon_detect.jpeg" class="card-image" alt="Weapon Detection" />
        </div>
        <p class="label">Weapon Detection</p>
      </div>
      <div class="card-block" @click="goTo('CriminalDetection')">
        <div class="card">
          <img src="/cop.jpeg" class="card-image" alt="Criminal Detection" />
        </div>
        <p class="label">Criminal Detection</p>
      </div>
      <div class="card-block" @click="goTo('CrowdManagement')">
        <div class="card">
          <img src="/Crowd-Management.jpg" class="card-image" alt="Crowd Management" />
        </div>
        <p class="label">Crowd Management</p>
      </div>
    </div>

    <router-link to="/" class="logout-button">Logout</router-link>
  </div>
</template>

<script>
export default {
  methods: {
    goTo(pageName) {
      // Use route names, not the path.
      this.$router.push({ name: pageName });
    }
  }
};
</script>

<style scoped>
.dashboard {
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  min-height: 100vh;
  color: #ffffff;
  padding: 30px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  overflow: hidden;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 90px;
  text-shadow: 0 0 10px #00bcd4;
}

.card-container {
  display: flex;
  justify-content: center;
  gap: 60px;
  margin-bottom: 50px;
  flex-wrap: wrap;
}

.card-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
}

.card {
  width: 250px;
  height: 250px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  box-shadow: 0 8px 20px rgba(0, 188, 212, 0.4);
  transition: transform 0.3s, box-shadow 0.3s;
  overflow: hidden;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 25px rgba(0, 188, 212, 0.6);
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
}

.label {
  margin-top: 12px;
  font-weight: bold;
  font-size: 1rem;
  color: #e0f7fa;
  text-shadow: 0 0 5px #00bcd4;
}

.logout-button {
  padding: 12px 30px;
  font-size: 1rem;
  background-color: #00bcd4;
  color: white;
  text-decoration: none;
  border-radius: 10px;
  transition: background-color 0.3s;
  margin-top: 20px;
}

.logout-button:hover {
  background-color: #0097a7;
}
</style>
