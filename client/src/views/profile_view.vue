<template>
  <div class="profile">
    <profile :key="loged_user.id" :user_info="loged_user"/>
  </div>
</template>

<script>
import axios from 'axios';
import profile from '@/components/profile.vue'

export default {
  name: "profile-view",
  components:{
    profile
  },
  data(){
    return{
      loged_user:{}
    }
  },
   methods:{
      check_user(){
        let user = this.$cookie.get('squarenetLogin')
        if(user != null){
            user = JSON.parse(user)
            this.loged_user = user
        }
        else{
          this.$router.push({name: 'homepage'})
        }
      },
      pass_data(){
        this.$emit('load', this.loged_user)
      },
      get_profile(user_id){
        axios.get('http://localhost:5000/user/profile/'+user_id).then(({data})=>{
          if(data != 'Profile not found'){
            this.loged_user.profile = data
            this.$cookie.set('squarenetLogin', JSON.stringify(this.loged_user), 5)
          }
        })
      },
  },
  beforeMount(){
    this.check_user()
    this.get_profile(this.loged_user.id)
    //this.check_gender()
    this.pass_data()
  }
}
</script>

<style>

</style>
