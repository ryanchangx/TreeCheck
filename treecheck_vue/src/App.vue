<template>
  <div id="wrapper">
    <nav class="navbar is-dark"> 
      <div class="navbar brand"> 
        <div id="wrapper">
        
        <!--A burger dropdown menu with 4 different options-->





        <!--<router-link to="/" class="navbar-item"><img alt="Vue logo" src="./assets/logo.png"></router-link>-->
          
          <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
              Menu
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#"><router-link to="/account" class="navbar-item">Account</router-link></a></li>
              <li><a class="dropdown-item" href="#"><router-link to="/friends" class="navbar-item">Friends</router-link></a></li>
              <li><a class="dropdown-item" href="#"><router-link to="/checklist" class="navbar-item">My List</router-link></a></li>
              <li><a class="dropdown-item" href="#"><router-link to="/leaderboard" class="navbar-item">Leaderboard</router-link></a></li>
            </ul>
          </div>
          
          
          </div>
        

        
      </div> 


    </nav> 
    <router-view/>
  </div>

</template>


<style scoped>
@import'~bootstrap/dist/css/bootstrap.css';
 /* Dropdown Button */
.dropbtn {
  background-color: #04AA6D;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: block;}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {background-color: #3e8e41;} 
</style>




<script>
import MenuBurger from '@/components/MenuBurger.vue'

export default {
  name: 'App'
}
</script>