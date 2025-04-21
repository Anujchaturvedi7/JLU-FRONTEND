<template>
    <div class="register-container">
      <h1>Register as:</h1>
      <div class="btn-container">
        <button @click="formType = 'user'">User</button>
        <button @click="formType = 'admin'">Admin</button>
      </div>
  
      <!-- User Registration -->
      <form v-if="formType === 'user'" class="form" @submit.prevent="submitUser">
        <h2>User Registration</h2>
        <input v-model="user.name" placeholder="Name" required />
        <input v-model="user.number" placeholder="Mobile Number" required />
        <input v-model="user.email" type="email" placeholder="Email" required />
        <input v-model="user.password" type="password" placeholder="Password" required />
        <button type="submit">Register as User</button>
      </form>
  
      <!-- Admin Registration -->
      <form v-if="formType === 'admin'" class="form" @submit.prevent="submitAdmin">
        <h2>Admin Registration</h2>
        <input v-model="admin.name" placeholder="Name" required />
        <input v-model="admin.number" placeholder="Mobile Number" required />
        <input v-model="admin.email" type="email" placeholder="Email" required />
        <input v-model="admin.passkey" placeholder="Passkey" required />
        <input v-model="admin.password" type="password" placeholder="Password" required />
        <button type="submit">Register as Admin</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'RegisterForm',
    data() {
      return {
        formType: null,
        API_URL: 'http://localhost:8000/register',
        user: {
          name: '',
          number: '',
          email: '',
          password: ''
        },
        admin: {
          name: '',
          number: '',
          email: '',
          passkey: '',
          password: ''
        }
      };
    },
    methods: {
      async submitUser() {
        if (!/^\d{10}$/.test(this.user.number)) return alert("Mobile must be 10 digits");
        if (this.user.email.includes("admin")) return alert("Email shouldn't include 'admin'");
  
        try {
          const res = await axios.post("http://localhost:8000/register/user", this.user);
          alert(res.data.message || 'User registered!');
        } catch (err) {
          console.error(err);
          if (err.response && err.response.data && err.response.data.detail) {
            alert(err.response.data.detail);
          }
          else {
          alert("User registration failed!");
        }
      }
      },
      async submitAdmin() {
        if (!/^\d{10}$/.test(this.admin.number)) return alert("Mobile must be 10 digits");
        if (this.admin.email.includes("user")) return alert("Email shouldn't include 'user'");
        if (this.admin.passkey !== '1234') return alert("Invalid passkey!");
  
        try {
          const res = await axios.post("http://localhost:8000/register/admin", this.admin);
          alert(res.data.message || 'Admin registered!');
        } catch (err) {
          console.error(err);
          if (err.response && err.response.data && err.response.data.detail) {
        alert(err.response.data.detail);  // Display backend error message (e.g., "Email already exists")
      }
          else{
            alert("Admin registration failed!");
          }
        }
      }
    }
  };
  </script>
  
  <style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

.register-container {
  font-family: 'Poppins', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  background-color: #0e0e0e;
  color: #f5f5f5;
}

h1 {
  margin-top: 50px;
  color: #00e5ff;
  font-size: 2.5rem;
  text-shadow: 0 0 15px #00ffd5;
}

.btn-container {
  margin: 30px;
  display: flex;
  gap: 20px;
}

button {
  margin: 10px;
  padding: 12px 25px;
  font-size: 16px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: #fff;
  box-shadow: 0 0 10px rgba(0, 255, 200, 0.3);
}

button:hover {
  transform: scale(1.05);
  box-shadow: 0 0 20px rgba(0, 255, 200, 0.5);
}

.btn-container button:first-child {
  background: linear-gradient(45deg, #00ffc6, #00bfff);
}

.btn-container button:last-child {
  background: linear-gradient(45deg, #ff416c, #ff4b2b);
}

.form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  width: 90%;
  max-width: 420px;
  background: #1c1c1c;
  padding: 30px 20px;
  border-radius: 20px;
  box-shadow: 0 10px 25px rgba(0, 255, 200, 0.2);
  animation: fadeIn 0.4s ease-in-out;
  border: 1px solid #333;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

input {
  width: 90%;
  padding: 12px;
  margin: 10px 0;
  border: 2px solid #444;
  background: #2a2a2a;
  color: #fff;
  border-radius: 10px;
  font-size: 15px;
  transition: border 0.3s ease, box-shadow 0.3s ease;
}

input:focus {
  border-color: #00ffd5;
  box-shadow: 0 0 8px #00ffd5;
  outline: none;
}

form button[type="submit"] {
  background: linear-gradient(90deg, #7f00ff, #e100ff);
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 10px;
  margin-top: 15px;
  font-size: 16px;
  font-weight: bold;
  transition: all 0.3s ease;
  box-shadow: 0 0 10px rgba(255, 0, 255, 0.3);
}

form button[type="submit"]:hover {
  background: linear-gradient(90deg, #e100ff, #7f00ff);
  box-shadow: 0 0 20px rgba(255, 0, 255, 0.5);
}
</style>
