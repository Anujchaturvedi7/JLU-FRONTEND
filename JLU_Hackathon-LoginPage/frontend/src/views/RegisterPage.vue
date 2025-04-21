<!-- <template>
    <div>
      <div>
        <button @click="tab = 'admin'">Register as Admin</button>
        <button @click="tab = 'user'">Register as User</button>
      </div>
      <div v-if="tab === 'admin'">
        <AdminRegister />
      </div>
      <div v-else>
        <UserRegister />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import AdminRegister from './AdminRegister.vue'
  import UserRegister from './UserRegister.vue'
  
  const tab = ref('admin')
  </script>
   -->