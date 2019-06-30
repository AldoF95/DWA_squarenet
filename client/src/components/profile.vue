<template>
    <div class="profile">
        <table class="profile-info">
            <tr>
                <td class="profile-image"><img :src="set_picture"/></td>
                <td class="profile-detail">
                    <table>
                        <tr><td><img src="../assets/user.png"/> {{user_info.name}}</td></tr>
                        <tr><td><img src="../assets/email.png"/> {{user_info.email}}</td></tr>
                        <tr><td><img src="../assets/settings.png"/><button class="settings-button" @click="display_settings">Profile settings</button></td></tr>
                    </table>
                    
                </td>
                <td class="profile-tags">
                    <table>
                        <tr><td>Tags</td></tr>
                        <tr><td>
                            <ul>
                                <li v-for="tags in user_info.profile.tags" :key="tags">{{tags}}</li>
                            </ul>
                        </td></tr>
                    </table>

                </td>
            </tr>
        </table>
        <transition name="settings">
                <ProfileSettings v-if="display_stg" :user_data="user_info"></ProfileSettings>
        </transition>
        
        <ProfilePosts v-for="post in posts_data" :key="post.id" :post_data="post" :user_logged="user_info"/>
    </div>
</template>

<style>
.settings-enter, .settings-leave-to{
    transform: translateY(-20px);
    opacity: 0;
}
.settings-enter-active{
    transition: all 0.3s ease-in;
}
.settings-leave-active{
    transition: all 0.1s ease-out;
}
.profile{
    margin: auto;
    width: 1025px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.profile .profile-info{
    padding-top: 30px;
    width: 100%;
    padding-bottom: 20px;
    border-bottom: 2px solid #012477;
}
.profile .profile-info .profile-image{
    width: 240px;
    padding: 20px;
}
.profile .profile-info .profile-image>img{
    height: 200px;
    border-radius: 45px;
    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.16);
    margin: 0;
    padding: 0;
    display: inline-block;
}
.profile .profile-info .profile-detail{
    height: 100%;
    border-right: 1.5px solid #7B7B7B;
}

.profile .profile-info .profile-detail>table{
    height: 200px;
}
.profile .profile-info .profile-detail>table>tr:nth-child(1){
    font-size: 1.5em;
    font-weight: bold;
}
.profile .profile-info .profile-detail>table>tr img{
    height: 1.2em;
    vertical-align: middle;
    margin-right: 10px;
}
.profile .profile-info .settings-button{
    background: none;
    border: none;
    text-decoration: underline;
}
.profile .profile-info .settings-button:hover{
    cursor: pointer;
    font-weight: bold;
}
.profile .profile-tags{
    padding-left: 20px;
}
.profile .profile-tags table>tr:nth-child(1) td{
    font-size: 1.5em;
    font-weight: bold;
    padding-left: 15px;
}
.profile .profile-tags table tr ul{
    list-style-type: circle;
}
.profile .profile-tags table tr ul li{
    padding: 5px 0px;
}


</style>

<script>
import axios from 'axios'
import ProfileSettings from '@/components/profile_settings'
import ProfilePosts from '@/components/posts'

export default {
    name: 'profile-header',
    props: ['user_info'],
    components:{
        ProfileSettings,
        ProfilePosts
    },
    data(){
        return{
            display_stg: false,
            posts_data: {},
            set_picture: "../assets/profile_male.png"
        }
    },
    mounted(){
        this.fetch_data(this.user_info.id)
        this.check_gender()
    },
    methods:{
        display_settings(){
            this.display_stg = !this.display_stg
        },
        fetch_data(user_id){
            axios.get('http://localhost:5000/profile_posts/'+ String(user_id)).then(({data})=>{
                if(data != 'No data'){
                    this.posts_data = data.data
                }
          })
        },
        check_gender(){
            if(this.user_info.profile.gender == 'M'){
                this.set_picture = require("../assets/profile_male.png")
            }
            else if(this.user_info.profile.gender == 'F'){
                this.set_picture = require("../assets/profile_female.png")
            }
            else{
                this.set_picture = require("../assets/profile_neutral.png")
            }
        }
    }
}
</script>
