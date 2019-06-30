<template>
    <div class="post" @click="hide_users" :style="{borderColor: border_color_post}">
        <table>
            <tr>
                <td><div class="profile_img" :style="{backgroundImage: 'url('+set_picture+')'}"/></td>
                <td><h1>{{post_data.title}}</h1></td>
            </tr>
            <tr>
                <td colspan="2">
                    <table class="data-info">
                        <tr>
                            <td><img src="../assets/time_w.png"/><span>{{post_data.due_time | moment('hh:mm')}}</span></td>
                            <td><img src="../assets/location_w.png"/><span>{{post_data.location}}</span></td>
                            <td><img src="../assets/people_w.png"/><span>{{post_data.need_users}}</span></td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td class="info-description"><img src="../assets/info.png"/><span>Description</span></td>
                <td class="info-description"><img src="../assets/calendar.png"/><span>{{post_data.due_time | moment('DD.MM.YY')}}</span></td>
            </tr>
            <tr style="min-height: 120px">
                <td class="data-description" colspan="2">
                    {{post_data.body}}
                </td>
            </tr>
            <tr>
                
                <td colspan="2">
                    <div class="user-add" @click="users_add_update" :style="{borderColor: border_color}" >
                        <span ref="users_count"  @mouseenter="show_users" >{{users_number}}</span>
                        <transition name="popup">
                        <UsersPopup v-if="popup_show" 
                                    :style="{postion:'absolute',top:popup_top, left:popup_left }"
                                    :user_data="post_data.apply_users"/>
                        </transition>
                    </div>
                    
                </td>
                
            </tr>
        </table>
        
        
        
    </div>
</template>

<script>
import axios from 'axios'
import UsersPopup from '@/components/apply_user.vue'


export default {
    name: 'post',
    props:['post_data', 'user_logged'],
    components: {UsersPopup},
    data(){
        return{
            users: this.post_data.apply_users,
            user_data: "",
            users_number: this.post_data.apply_users.length,
            popup_show: false,
            popup_top: 0,
            popup_left: 0,
            user_add:{
                id: this.user_logged.id,
                name: this.user_logged.name,
                gender: this.user_logged.profile.gender
            },
            border_color: '#012477',
            border_color_post: '#707070',
            set_picture: require("../assets/profile_neutral.png")
            }
        },

    methods:{
        users_add(){
            if(this.post_data.apply_users===[]){
                return this.users = 0
            }
            else{
                return this.users = this.post_data.apply_users.length
            }
        },
        users_add_update(){
            if(!this.check_apply_user()){
                this.post_data.apply_users.push(this.user_add)
                this.users_number += 1
                this.check_apply_user()
                axios.put('http://localhost:5000/posts', {
                    post_id: this.post_data.id,
                    apply_users: this.post_data.apply_users
                }).then()
            }
            
        },
        get_user_data(){
            axios.get('http://localhost:5000/user/profile/'+this.post_data.user).then(({data})=>{
                if(data != 'Profile not found'){
                        this.user_data = data
                        this.check_gender()
                    }
                })
        },
        check_apply_user(){
            for(let u of this.post_data.apply_users){
                if(u.id==this.user_add.id){
                    this.border_color = 'lime'
                    return true
                }
            }
        },
        check_post_user(){
            if(this.user_logged.id == this.post_data.user){
                this.border_color_post = 'lime'
            }
            if(this.users_number >= this.post_data.need_users){
                this.border_color_post = 'orange'
            }
        },
        show_users(){
            let top = this.$refs.users_count.getBoundingClientRect().top - 30
            let left = this.$refs.users_count.getBoundingClientRect().left + 30
            this.popup_top = String(top) + "px"
            this.popup_left = String(left) + "px"
            this.popup_show = !this.popup_show
        },
        hide_users(){
            if(this.popup_show == true){
                this.popup_show = !this.popup_show
            }
            
        },
        check_gender(){
            if(this.user_data.gender == 'M'){
                this.set_picture = require("../assets/profile_male.png")
            }
            else if(this.user_data.gender == 'F'){
                this.set_picture = require("../assets/profile_female.png")
            }
            else{
                this.set_picture = require("../assets/profile_neutral.png")
            }
        }
    },
    created(){
        this.check_apply_user()
        
    },
    mounted(){
        this.check_post_user()
        
    },
    beforeMount(){
        this.get_user_data()
    },
    computed:{
        users_2 : function(){
            return this.users_add()
        }
    },
}
</script>

<style>
.popup-enter, .popup-leave-to{
    opacity: 0;
    transform: translateX(-10px);
}
.popup-enter-active{
    transition: all 0.2s ease-in;
}
.popup-leave-active{
    transition: all 0.2s ease-out;
}
.post{
    display: inline-block;
    height: 400px;
    width: 315px;
    border-radius: 100px 13px 100px 13px;
    border: 1px solid;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.16);
    margin-right: 20px;
    margin-top: 30px;
}
.post > table{
    width: 100%;
    height: 100%;
    top: 0;
    bottom: 0;
}
.post .profile_img{
    display: inline-block;
    /*background-image: url("../assets/profile_female.png");*/
    background-repeat: no-repeat;
    background-size: 120%;
    background-position: center;
    margin: 0;
    height: 75px;
    width: 75px;
    border-radius: 50%;
    box-shadow: 5px 5px 6px rgba(0, 0, 0, 0.16);
}
.post h1{
    color: #012477;
    font-size: 25px;
}

.post table .data-info{
    background-color: #012477;
    height: 42px;
    width: 300px;
    border-radius: 21px;
    color: #E9E9E9;
    margin: auto;

}
.post table .data-info td{
    padding-left: 7px;
}
.post table .data-info td span{
    padding-left: 7px;
}

.post table .data-info td:nth-child(1), .post table .data-info td:nth-child(2){
    border-right: 1px solid #E9E9E9;
} 

.post table ul{
    height: 42px;
    width: 300px;
    padding: 0;

    margin: auto;
    background-color:#012477;
    color:  #E9E9E9;
    font-size: 15px;
    border-radius: 21px;
    list-style-type: none;
    vertical-align: middle;
}
.post table li{
    float: left;
    text-align: center;
    vertical-align: middle;
}

.post table li span{
    padding-left: 14px;
}
.post > table img{
    height: 30px;
    vertical-align: middle;
}

.post table .user-add{
    margin: auto;
    height: 70px;
    width: 70px;
    background-image: url('../assets/user_add.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size: 90%;
    border: 2px solid;
    border-radius: 21px;
    box-shadow: -3px 3px 6px rgba(0, 0, 0, 0.16);
}
.post table .data-description{
    font-size: 14px;
    line-height: 19px;
    padding-left: 20px;
    padding-right: 20px;
    min-height: 120px;
}
.post table .user-add span{
    font-size: 12px;
    margin-top: -10px;
    margin-right: -10px;
    float:right;
    color:#E9E9E9;
    height: 28px;
    min-width: 28px;
    text-align: center;
    vertical-align: middle;
    background-color: #012477;
    border-radius: 14px;
    line-height: 2.2;
}
.post table .user-add:hover{
    cursor: pointer;
}

.post table .info-description{
    padding-left: 15px;
}
.post table .info-description span{
    padding-left: 10px;
}
</style>
