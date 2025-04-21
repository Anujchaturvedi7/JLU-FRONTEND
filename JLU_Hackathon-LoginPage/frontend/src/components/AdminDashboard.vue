<template>
    <div class="dashboard">
      <h1>Welcome, Admin!</h1>
      <p>This is your admin panel.</p>
      <button @click="logout">Logout</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminDashboard',
    methods: {
      logout() {
        // Clear session/token if you’re using one
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .dashboard {
    max-width: 600px;
    margin: 100px auto;
    padding: 30px;
    background-color: #f0f0f0;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
  
  h1 {
    color: #2196f3;
    margin-bottom: 15px;
  }
  
  button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #f44336;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
  }
  
  button:hover {
    background-color: #d32f2f;
  }
  </style>
  