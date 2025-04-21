<!-- <template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="email" placeholder="Email" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <router-link to="/register">Register!</router-link></p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  const email = ref('')
  const password = ref('')
  const router = useRouter()
  
  const login = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login', {
        email: email.value,
        password: password.value
      })
      const role = response.data.role
      if (role === 'admin') router.push('/admin')
      else if (role === 'user') router.push('/user')
      else alert('Invalid role')
    } catch (err) {
      alert('Login failed!')
    }
  }
  </script>
   -->