<template>
  <div class="home">

      <post_search :logged_user="loged_user"/>
      <posts v-for="post in posts_data" 
        v-bind:key="post.id"
        :post_data="post"
        :user_logged="loged_user"/>
  </div>
</template>

<script>
import axios from 'axios';
import posts from '@/components/posts.vue'
import post_search from '@/components/new_post_search.vue'

export default {
  name: "home",
  components:{
    posts,
    post_search
  },
  data(){
       return {
           posts_data:{},
           loged_user:{}
        }
  },
  mounted(){
      this.fech_data()
      this.pass_data()
  },
  methods:{
      fech_data(){
          axios.get('http://localhost:5000/posts').then(({data})=>{
              this.posts_data = data.data
          })
      },
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
      async create_profile(id_user, status){
        if(status==true){
          await axios.post('http://localhost:5000/profile', {
            user_id: id_user
          }).then(()=>{
            this.loged_user.new_user=false
            console.log('profile created')
          })
        }
      }
  },
  beforeMount(){
    this.check_user()
    this.create_profile(this.loged_user.id, this.loged_user.new_user).then(
      this.get_profile(this.loged_user.id)
    )
  }
}
</script>

<style>
.home{
    width: 1025px;
    margin: auto;
}
</style>