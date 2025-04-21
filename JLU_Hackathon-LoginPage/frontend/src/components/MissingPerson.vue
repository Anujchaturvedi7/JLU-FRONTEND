<template>
  <div class="missing-persons">
    <h1>Missing Persons Report</h1>

    <div v-if="missingPersons.length === 0" class="no-data">
      <p>No missing persons data available.</p>
    </div>

    <div v-else class="person-cards">
      <div v-for="person in missingPersons" :key="person.name" class="person-card">
        <img :src="person.photo_url" alt="Missing Person Photo" class="person-photo" />
        <div class="person-details">
          <h2>{{ person.name }}</h2>
          <p>Status: <span :class="{'found': person.status === 'Found', 'not-found': person.status !== 'Found'}">
            {{ person.status }}</span></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      missingPersons: [],
    };
  },
  mounted() {
    this.fetchMissingPersons();
  },
  methods: {
    async fetchMissingPersons() {
      try {
        // Replace with your actual API endpoint
        const response = await fetch("https://your-backend-api/missing-persons");
        if (response.ok) {
          const data = await response.json();
          this.missingPersons = data;
        } else {
          console.error("Failed to fetch missing persons data");
        }
      } catch (error) {
        console.error("Error fetching missing persons data:", error);
      }
    },
  },
};
</script>

<style scoped>
.missing-persons {
  text-align: center;
  background-color: #121212;
  color: #fff;
  padding: 30px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  font-size: 2.5rem;
  color: #00bcd4;
  margin-bottom: 30px;
  text-shadow: 0 0 15px #00bcd4, 0 0 20px #00bcd4;
}

.no-data {
  color: #777;
}

.person-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.person-card {
  background-color: #1a1a1a;
  border-radius: 10px;
  padding: 20px;
  width: 250px;
  box-shadow: 0 4px 8px rgba(0, 188, 212, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
  text-align: center;
}

.person-card:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 25px rgba(0, 188, 212, 0.6);
}

.person-photo {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 15px;
}

.person-details h2 {
  font-size: 1.2rem;
  font-weight: bold;
  color: #00bcd4;
  text-shadow: 0 0 10px #00bcd4;
}

.person-details p {
  font-size: 1rem;
  color: #e0e0e0;
}

.found {
  color: #66ff66;
  font-weight: bold;
  text-shadow: 0 0 10px #66ff66;
}

.not-found {
  color: #ff4d4d;
  font-weight: bold;
  text-shadow: 0 0 10px #ff4d4d;
}
</style>
