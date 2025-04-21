<template>
  <div class="login-wrapper">
    <div class="login-container">
      <h2>Login User/Admin</h2>
      <form @submit.prevent="handleLogin">
        <label for="email">Email</label>
      <input type="email" v-model="email" placeholder="Enter your email" required />
  
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" placeholder="Enter your password" required />
  
        <button type="submit">Login</button>
      </form>
      <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
      <p class="note">Don’t have an account? <router-link to="/register">Register here</router-link></p>
    </div>
  </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
        errorMsg: ''
      };
    },
    methods: {
  async handleLogin() {
    // Validate email format
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(this.email)) {
      this.errorMsg = "Please enter a valid email address.";
      return;
    }

    if (!this.password) {
      this.errorMsg = "Password cannot be empty.";
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email: this.email,  // ✅ Use 'username' key if FastAPI OAuth expects it
          password: this.password
        })
      });

      const data = await response.json();

      if (response.ok && data.access_token) {
        const token = data.access_token;
        const decoded = JSON.parse(atob(token.split('.')[1])); // Decode JWT

        localStorage.setItem("token", token); // Store token if needed

        if (decoded.role === "user") {
          this.$router.push('/UserDashboard');  // ✅ lower-case, hyphenated

        } else if (decoded.role === "admin") {
          this.$router.push('/AdminDashboard');  // ✅


        } else {
          this.errorMsg = "Unknown user role.";
        }

      } else {
        this.errorMsg = data.detail || "Invalid login credentials.";
      }

    } catch (error) {
      console.error("Login error:", error);
      this.errorMsg = "An error occurred while logging in. Please try again.";
    }
  }
}

    // methods: {
    //   async handleLogin() {
    //     // Validate email format
    //     const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    //     if (!emailPattern.test(this.email)) {
    //       this.errorMsg = "Please enter a valid email address.";
    //       return;
    //     }
  
    //     if (!this.password) {
    //       this.errorMsg = "Password cannot be empty.";
    //       return;
    //     }
  
    //     try {
    //       const response = await fetch("http://localhost:8000/login", {
    //         method: "POST",
    //         headers: {
    //           "Content-Type": "application/json"
    //         },
    //         body: JSON.stringify({
    //           email: this.email,
    //           password: this.password
    //         })
    //       });
  
    //       const data = await response.json();
  
    //       if (response.ok && data.status === "success") {
    //         if (data.role === "user") {
    //           window.location.href = "user-dashboard.html";
    //         } else if (data.role === "admin") {
    //           window.location.href = "admin-dashboard.html";
    //         } else {
    //           this.errorMsg = "Unknown user role.";
    //         }
    //       } else {
    //         this.errorMsg = data.message || "Invalid login credentials.";
    //       }
  
    //     } catch (error) {
    //       console.error("Login error:", error);
    //       this.errorMsg = "An error occurred while logging in. Please try again.";
    //     }
    //   }
    // }
  };
  </script>
  
  <style scoped>
/* Important note: body styles must be added to global CSS (not scoped) for full effect */

.login-wrapper {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container {
  background: linear-gradient(135deg, #1e1e1e, #2b2b2b);
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 229, 255, 0.3);
  width: 380px;
  transition: 0.3s;
}

.login-container:hover {
  box-shadow: 0 0px 25px rgba(0, 229, 255, 0.3);
}

h2 {
  margin-bottom: 20px;
  text-align: center;
  color: #00e5ff;
  text-shadow: 0 0 20px rgba(0, 229, 255, 0.3);
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

label {
  font-weight: bold;
  color: #cccccc;
}

input {
  padding: 10px;
  border: 1px solid #444;
  background-color: #1e1e1e;
  color: #fff;
  border-radius: 8px;
  font-size: 16px;
  transition: 0.2s;
}

input:focus {
  outline: none;
  border-color: #00ffc3;
  box-shadow: 0 0 8px #00ffc3;
}

button {
  padding: 12px;
  background: linear-gradient(90deg, #00ffc3, #00b3ff);
  color: #000;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.3s ease;
}

button:hover {
  background: linear-gradient(90deg, #00b3ff, #00ffc3);
}

.note {
  margin-top: 15px;
  font-size: 14px;
  text-align: center;
  color: #aaa;
}

.note a {
  color: #00ffc3;
  text-decoration: none;
  font-weight: bold;
}

.note a:hover {
  text-decoration: underline;
}

.error-msg {
  color: #ff4d4d;
  text-align: center;
  margin-top: 10px;
  font-weight: bold;
  text-shadow: 0 0 6px #ff4d4d;
}
</style>
