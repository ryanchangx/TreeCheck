<template>
  <form @submit.prevent="logIn">
    <input v-model="username" />
    <input type="password"/>
    <button>Login!</button>
  </form>
</template>
<script>
import router from '../router'
  export default {
      data(){
        return{
            username: ""
        }
      },
      methods: {
          logIn(){
            $cookies.set('loggedIn', 'true');
            $cookies.set('username', this.username);
            let dataa = {username: this.username};
            
            fetch('http://128.199.5.103:8181/api/v1/userlogin/',{
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(dataa)
            }).then(function(response) {
                return response.json();
            }).then((data) => {
                $cookies.set('user_id', data.id);
            });
            setTimeout(function(){
                fetch('http://128.199.5.103:8181/api/v1/userlogin/',{
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(dataa)
                }).then(function(response) {
                    return response.json();
                }).then((data) => {
                    $cookies.set('user_id', data.id);
                    $cookies.set('username', data.username)
                });
            }, 500);
            router.push("/account");
          }
      },
      name: 'LoginView',
  };
</script>