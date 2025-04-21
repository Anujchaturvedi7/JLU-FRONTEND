<!-- <template>
  <div class="register-container">
    <h2>Register as Admin</h2>
    <form @submit.prevent="registerAdmin">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <input v-model="passkey" type="text" placeholder="Secret Passkey" required />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      email: '',
      password: '',
      passkey: ''
    }
  },
  methods: {
    async registerAdmin() {
      try {
        await axios.post('http://127.0.0.1:8000/register/admin', {
          email: this.email,
          password: this.password,
          passkey: this.passkey
        })
        alert('Admin registered successfully!')
        this.$router.push('/login')
      } catch (error) {
        alert('Registration failed. Please check passkey or try again.')
        console.error(error)
      }
    }
  }
}
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 0 auto;
}
</style> -->
