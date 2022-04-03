import { createApp } from 'vue'
import { createAuth0 } from '@auth0/auth0-vue';

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import router from './router'
import store from './store'
import bootstrap from 'bootstrap';
import axios from 'axios';


axios.defaults.baseURL = 'http://128.199.5.103:8181';

createApp(App).use(store).use(router, axios).use(bootstrap).mount('#app')
//createApp(App).use(store).use(router).use(BootstrapVue).use(IconsPlugin).mount('#app')
