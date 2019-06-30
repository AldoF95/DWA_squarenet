<template>
  <div id='app'>
    <div v-if="home" class="navigation">

      <nav>
        <router-link class="home" :to="{name: 'home'}"></router-link>
        <table>
          <tr>
            <td><router-link class="profile_img" :style="{backgroundImage: 'url('+set_picture+')'}" :to="{name: 'profile'}"/></td>
            <td><router-link class="profile_name" :to="{name:'profile'}">{{user.name}}</router-link></td>
            <td><img ref="notif_list" src="./assets/notification_w.png" @click="show_toggle"/></td>

            <td><a class="logout" href="" @click="logout()"/></td>
          </tr>
        </table>
      </nav>
    </div>
    <transition name="notif-popup">
      <notifications v-if="show_notif" 
                    :user_id="user.id"
                    :style="{postion:'absolute',top:popup_top, left:popup_left }"
                    />
    </transition>
    
    <div class="content">
      <router-view @load="getData"></router-view>
    </div>
        
  </div>
</template>

<style>
.notif-popup-enter, .notif-popup-leave-to{
    opacity: 0;
    transform: translateY(-10px);
}
.notif-popup-enter-active{
    transition: all 0.2s ease-in;
}
.notif-popup-leave-active{
    transition: all 0.2s ease-out;
}

.content{
  margin-top: 50px;
}
.navigation{
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  background-color: #012477;
  height: 50px;
  padding: 0;
  margin: 0;
  top: 0;
  left: 0;
  right: 0;
  position: absolute;
}

.navigation nav{
  margin: auto;
  width: 1025px;
  height: 100%;
  padding-top: 5px;
  vertical-align: middle;
}

nav table{
  color: #FFFFFF;
  float: right;
  padding: 0;
  height: 40px;
}
nav > .home{
  display: inline-block;
  background-image: url('./assets/squarenet_logo.png');
  background-position: center;
  background-size: cover;
  height: 40px;
  width: 40px;
  
}
nav .profile_img{
  display: inline-block;
  padding: 0;
  margin: 0;
  height: 35px;
  width: 35px;
  /*background-image: url('./assets/profile_female.png');*/
  background-position: center;
  background-size: 120%;
}

nav table .profile_name{
  color: #FFFFFF;
  text-decoration: none;
  padding-left: 10px;
  padding-right: 10px;

}


nav table td:nth-child(2), nav table td:nth-child(3){
  border-right: 1px solid #ffffff;
} 
nav table span{
  padding-left: 10px;
  padding-right: 10px;
}

nav .logout{
  display: inline-block;
  background-image: url('./assets/logout_w.png');
  background-position: center;
  background-size: cover;
  height: 25px;
  width: 25px;
  margin-left: 10px;
  margin-right: 10px;
  
}
nav table img{
  height: 25px;
  padding-left: 10px;
  padding-right: 10px;
}
nav table img:hover{
  cursor: pointer;
}
</style>

<script>
import notifications from '@/components/notification.vue'

export default {
  name: 'App',
  components: {notifications},
  data(){
    return{
      user:{},
      set_picture: require("./assets/profile_female.png"),
      show_notif: false,
      popup_top: 0,
      popup_left: 0,
    }
  },
  computed:{
    home(){
      let p = this.$route.path
      if(p==='/'){return false}
      else{return true}
    }
  },
  mounted(){
    this.check_gender()
  },
  methods:{
    getData(d){
      this.user=d
    },
    logout(){
      this.$cookie.delete('squarenetLogin')
      this.$router.push({name: 'homepage'})
    },
    check_gender(){
      if(this.user.profile.gender == 'M'){
        this.set_picture = require("./assets/profile_male.png")
      }
      else if(this.user.profile.gender == 'F'){
        this.set_picture = require("./assets/profile_female.png")
      }
      else{
        this.set_picture = require("./assets/profile_neutral.png")
      }
    },
    show_toggle(){
        let top = this.$refs.notif_list.getBoundingClientRect().top + 43
        let left = this.$refs.notif_list.getBoundingClientRect().left - 285
        this.popup_top = String(top) + "px"
        this.popup_left = String(left) + "px"
        this.show_notif = !this.show_notif
    }
  }
}
</script>

