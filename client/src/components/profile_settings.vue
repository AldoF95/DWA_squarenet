<template>
    <div class="profile-settings">
        <div class="container">
        <div class="menu">
            <table>
                <tr :style="[show == 'general'? {backgroundColor: active} : {backgroundColor: non_active}]"><td @click="change_show('general')">General</td></tr>
                <tr :style="[show == 'password'? {backgroundColor: active} : {backgroundColor: non_active}]"><td @click="change_show('password')">Password</td></tr>
                <tr :style="[show == 'notification'? {backgroundColor: active} : {backgroundColor: non_active}]"><td @click="change_show('notification')">Notification</td></tr>
                <tr :style="[show == 'privacy'? {backgroundColor: active} : {backgroundColor: non_active}]"><td @click="change_show('privacy')">Privacy</td></tr>
                <tr :style="[show == 'policy'? {backgroundColor: active} : {backgroundColor: non_active}]"><td @click="change_show('policy')">Privacy Policy</td></tr>
            </table>
        </div>
        <div class="settings-content">
            <section class="general" v-if="show == 'general'">
                <table>
                    <tr>
                        <td>Username:</td>
                        <td><input type="text" name="username" placeholder="username" v-model="update_data.name" /></td>
                    </tr>
                    <tr>
                        <td>Email:</td>
                        <td><input type="email" name="email" placeholder="email" v-model="update_data.email"/></td>
                    </tr>
                    <tr>
                        <td>Tags:</td>
                        <td><select><option v-for="tag in user_data.profile.tags" :key="tag">{{tag}}</option></select></td>
                    </tr>
                    <tr>
                        <td>Gender:</td>
                        <td>
                            <select v-model="update_data.gender">
                            <option v-for="g in genders" :key="g" :selected="g == update_data.gender" :value="g" >{{g}}</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>Age:</td>
                        <td><input type="email" name="email" placeholder="email" v-model="update_data.age"/></td>
                    </tr>
                    <tr>
                        <td>Description:</td>
                        <td><textarea name="description" placeholder="description" v-model="update_data.description"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><button @click="update_profile">Save changes</button></td>
                    </tr>
                </table>
            </section>
            <section class="password" v-if="show == 'password'">
                <table>
                    <tr>
                        <td>Current password</td>
                        <td><input type="password" name="password" placeholder="pass" v-model="update_data.old_password"/></td>
                    </tr>
                    <tr>
                        <td>New password</td>
                        <td><input type="password" name="new_password"  value="" v-model="update_data.new_password"/></td>
                    </tr>
                    <tr>
                        <td>Repeat new password</td>
                        <td><input type="password" name="new_password_r"  value=""/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><button>Change password</button></td>
                    </tr>
                </table>
            </section>
            <section class="notification" v-if="show == 'notification'">
                notification
            </section>
            <section class="privacy" v-if="show == 'privacy'">
                privacy
            </section>
            <section class="policy" v-if="show == 'policy'">
                policy
            </section>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'profile-settings',
    props: ['user_data'],
    data(){
        return{
            show: 'general',
            active: '#3889FF',
            non_active: '#012477',
            genders: ['M', 'F', 'N'],
            update_data:{
                email: this.user_data.email,
                name: this.user_data.name,
                gender: this.user_data.profile.gender,
                age: this.user_data.profile.age,
                description: this.user_data.profile.description,
                new_password: "",
                old_password: ""
            }
        }
    },
    methods:{
        change_show(target){
            this.show = target
        },
        update_profile(){
            axios.put('http://localhost:5000/profile',{
                id : this.user_data.profile.id,
                gender : this.update_data.gender,
                age : this.update_data.age,
                description :  this.update_data.description 
            }).then(
                axios.put('http://localhost:5000/user',{
                    id: this.user_data.id,
                    name : this.update_data.name
                }).then(
                    this.$router.push({name: 'home'})
                )
            )
            
        },
    }
    
}
</script>

<style>
.profile-settings .container{
    display: block !important;
    min-width: 1000px !important;
     font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.profile-settings div{
    display: inline;
    margin: auto;
    float: left;
}
.profile-settings .menu table:nth-child(1){
    padding: 25px 8px;
    background-color: #012477;
    color: #ffffff;
    margin-top: 20px;
    border-radius: 45px 5px;
    box-shadow: 6px 6px 10px rgba(0,0,0,0.16);
}
.profile-settings .menu table tr{
    width: 100%;
    margin: 0;
    padding: 0;
    border-radius: 10px;
}
.profile-settings .menu table td{
    margin: 0;
    padding: 5px 10px;
    border-radius: 10px;
}
.profile-settings .menu table tr:hover{
    cursor: pointer;
    background-color: #ffffff !important; 
    color: #012477;
}
.profile-settings .settings-content{
    padding-left: 100px;
    margin-top: 30px;
}
.profile-settings .settings-content .general table{
    width: 500px;
    border-collapse: separate;
    border-spacing: 0 20px;
}
.profile-settings .settings-content .general table input{
    height: 25px;
    width: 200px;
    font-size: 1.07em;
    border: 1px solid #012477;
    border-radius: 3px;
    padding-left: 8px;
    margin-left: 50px;
}
.profile-settings .settings-content .general table textarea{
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    height: 100px;
    width: 200px;
    font-size: 0.9em;
    border: 1px solid #012477;
    border-radius: 3px;
    padding-left: 8px;
    margin-left: 50px;
}
.profile-settings .settings-content .general table select{
    height: 25px;
    width: 210px;
    font-size: 1.07em;
    border: 1px solid #012477;
    border-radius: 3px;
    padding-left: 8px;
    margin-left: 50px;
}
.profile-settings .settings-content .general table tr>td:nth-child(1){
    text-align: right;
}
.profile-settings .settings-content .general table tr td button{
        margin-left: 50px;
        padding: 5px 10px;
        height: 30px;
        background: none;
        border: 1.5px solid #012477;
        border-radius: 15px;
        font-weight: bold;
        box-shadow: 3px 3px 6px rgba(0,0,0,0.16)
}
.profile-settings .settings-content .general table tr td button:hover{
    cursor: pointer;
    background-color: #012477;
    color: #ffffff;
}
.profile-settings .settings-content .password table{
    width: 500px;
    border-collapse: separate;
    border-spacing: 0 20px;
}
.profile-settings .settings-content .password table input{
    height: 25px;
    width: 200px;
    font-size: 1.07em;
    border: 1px solid #012477;
    border-radius: 3px;
    padding-left: 8px;
    margin-left: 50px;
}
.profile-settings .settings-content .password table tr>td:nth-child(1){
    text-align: right;
}
.profile-settings .settings-content .password table tr:nth-child(4)>td:nth-child(1){
    text-align: center;
}
.profile-settings .settings-content .password table tr td button{
        margin-left: 50px;
        padding: 5px 10px;
        height: 30px;
        background: none;
        border: 1.5px solid #012477;
        border-radius: 15px;
        font-weight: bold;
        box-shadow: 3px 3px 6px rgba(0,0,0,0.16)
}
.profile-settings .settings-content .password table tr td button:hover{
    cursor: pointer;
    background-color: #012477;
    color: #ffffff;
}
</style>


