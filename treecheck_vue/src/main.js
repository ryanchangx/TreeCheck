import { createApp } from 'vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import router from './router'
import store from './store'
import bootstrap from 'bootstrap';
import axios from 'axios';
import { globalCookiesConfig } from "vue3-cookies";
import VueCookies from 'vue-cookies'

globalCookiesConfig({
    expireTimes: "30d",
    path: "/",
    domain: "",
    secure: false,
    sameSite: "None",
  });

if($cookies.get('loggedIn' != 'true')){
    $cookies.set('loggedIn', 'false');
 }
  

axios.defaults.baseURL = 'http://128.199.5.103:8181';

createApp(App).use(store).use(router, axios).use(bootstrap).mount('#app')

//createApp(App).use(store).use(router).use(BootstrapVue).use(IconsPlugin).mount('#app')
