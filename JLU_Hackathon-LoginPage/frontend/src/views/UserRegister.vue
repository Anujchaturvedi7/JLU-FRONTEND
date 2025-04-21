<!-- <template>
    <div>
      <h2>Register as User</h2>
      <form @submit.prevent="register">
        <input v-model="email" placeholder="Email" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const email = ref('')
  const password = ref('')
  
  const register = async () => {
    try {
      await axios.post('http://localhost:8000/register/user', {
        email: email.value,
        password: password.value,
        role: 'user'
      })
      alert('User registered successfully!')
    } catch (err) {
      alert('Registration failed!')
    }
  }
  </script>
   -->