// import { createRouter, createWebHistory } from 'vue-router'
// import LoginForm from '../views/LoginForm.vue'
// import RegisterPage from '../views/RegisterPage.vue'
// import AdminPortal from '../components/AdminPortal.vue'
// import UserPortal from '../components/UserPortal.vue'

// const routes = [
//   { path: '/', name: 'Login', component: LoginForm },
//   { path: '/register', name: 'Register', component: RegisterPage },
//   { path: '/admin', name: 'AdminPortal', component: AdminPortal },
//   { path: '/user', name: 'UserPortal', component: UserPortal },
// ]

// const router = createRouter({
//   history: createWebHistory(),
//   routes
// })

// export default router
import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/components/LandingPage.vue';
import LoginForm from '@/components/LoginForm.vue';
import RegisterForm from '@/components/RegisterForm.vue';
import UserDashboard from '@/components/UserDashboard.vue';
import AdminDashboard from '@/components/AdminDashboard.vue';
import MissingPerson from '@/components/MissingPerson.vue';
import WeaponDetection from '@/components/WeaponDetection.vue';
import CriminalDetection from '@/components/CriminalDetection.vue';
import CrowdManagement from '@/components/CrowdManagement.vue';


const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: LoginForm },
  { path: '/register', component: RegisterForm },
  { path: '/UserDashboard', component: UserDashboard },
  { path: '/AdminDashboard', component: AdminDashboard },
  { path: '/MissingPerson', component: MissingPerson, name: 'MissingPerson' },
  { path: '/WeaponDetection', component: WeaponDetection, name: 'WeaponDetection' },
  { path: '/CriminalDetection', component: CriminalDetection, name: 'CriminalDetection' },
  { path: '/CrowdManagement', component: CrowdManagement, name: 'CrowdManagement' },
  { path: '/', redirect: '/login' }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
