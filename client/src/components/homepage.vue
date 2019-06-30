<template>
    <div class="content-box">
        <div class="content-left">
            <table>
                <tr>
                    <td colspan="2">
                        <img class="logo-img" src="../assets/squarenet_logo.png"/>
                        <h1>SQUARENET</h1>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>Connect with new people and forget the boring 
                        afternoons spent doing nothing</p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img src="../assets/arrow_w.png"/>
                        <span>Meet new friends</span>
                    </td>
                    <td>
                        <img src="../assets/arrow_w.png"/>
                        <span>Find activities</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img src="../assets/arrow_w.png"/>
                        <span>Create new activities</span>
                    </td>
                    <td>
                        <img src="../assets/arrow_w.png"/>
                        <span>Spend quality time</span>
                    </td>
                </tr>
            </table>
        </div>
        <div class="content-right">
            <div class="menu-top">
                <router-link class="Login" :to="{name: 'homepage'}">Login</router-link>
                <router-link class="Register" :to="{name: 'register'}">Register</router-link>
            </div>
            <form class='login-form' v-if="login">
                <table>
                    <tr>
                        <td colspan="2"><h2>Login with email</h2></td>
                    </tr>
                    <tr>
                        <td><input :style="{borderBottomColor: border_color}" type="email" name="email" v-model="input.email" placeholder="Email"/></td>
                        <td><img src="../assets/email.png"/></td>
                    </tr>
                    <tr>
                        <td><input :style="{borderBottomColor: border_color}" type="password" name="pass" v-model="input.password" placeholder="Password"/></td>
                        <td><img src="../assets/password.png"/></td>
                    </tr>
                    <tr>
                        <td colspan="2"><button @click.prevent="login_user()">Login</button></td>
                    </tr>
                </table>                
            </form>
            <form class="register-form" v-if="register">
                <table>
                    <tr>
                        <td colspan="2"><h2>Register here</h2></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="user" placeholder="Username" v-model="input.username"/></td>
                        <td><img src="../assets/user.png"/></td>
                    </tr>
                    <tr>
                        <td><input type="email" name="email" placeholder="Email" v-model="input.email"/></td>
                        <td><img src="../assets/email.png"/></td>
                    </tr>
                    <tr>
                        <td><input type="password" name="pass" placeholder="Password" v-model="input.password"/></td>
                        <td><img src="../assets/password.png"/></td>
                    </tr>
                    <tr>
                        <td colspan="2"><button @click.prevent="register_user()">Register</button></td>
                    </tr>
                </table> 
            </form>
        </div>
    </div>
</template>

<style>
.content-box{
    position:absolute;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    padding: 0;
    margin: 0;
    top: 0;
    bottom: 0;
    left:0;
    right: 0;
    height: 100%;
    width: 100%;
    background-image: url('../assets/background.jpg');
    background-position: center;
    background-size: cover;
}

.content-left{
    float: left;
    margin: 0;
    background-image: linear-gradient(141deg, rgba(159, 184, 173, 0.8) 0%, rgba(31, 200, 219, 0.7) 51%, rgba(44, 181, 232, 0.6) 75%);
    width: 50%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #ffffff;
}
.content-right{
    float: left;
    margin: 0;
    width: 50%;
    height: 100%;
}
.content-left table{
    color: #ffffff;
    width: 60%;
    margin: auto;
    border-collapse: separate;
    border-spacing: 0 30px;
}
.content-left table tr:nth-child(1){
    text-align: center;
}
.content-left table img{
    vertical-align: middle;
    height: 15px;
}
.content-left table .logo-img{
    vertical-align: middle;
    height: 60px;
}
.content-left table h1{
    margin-left: 20px;
    vertical-align: middle;
    display: inline;
    color: #F1FF6C;
}
.content-left table p{
    font-size: 1.2em;
    border: 1.2px solid #F1FF6C;
    padding: 10px 20px;
}

.content-left table span{
    padding-left: 20px;
}

.content-right .login-form{
    width: 40%;
    min-width: 300px;
    /*background-image: linear-gradient(141deg, rgba(159, 184, 173, 0.8) 0%, rgba(31, 200, 219, 0.7) 50%, rgba(44, 181, 232, 0.6) 71%);*/
    background-color: rgba(255, 255, 255, 0.8);
    padding: 0px 0px;
    margin: auto;
    margin-top: 30%;
    box-shadow: 10px 10px 6px rgba(0, 0, 0, 0.16);

}
.login-form table{
    margin: auto;
    text-align: center;
    border-collapse: separate;
    border-spacing: 0 30px;
}
.login-form table tr:nth-child(1) td:nth-child(1){
    border-bottom: 1px solid #6f6f6f;
}
.login-form table img{
    height: 30px;
    vertical-align: middle;
}
.login-form table input{
    border: none;
    width: 200px;
    height: 2em;
    font-size: 1.1em;
    border-bottom: 1px solid rgb(31, 200, 219);
    background: none;
    padding-left: 10px;
}
.login-form table button{
    width: 80px;
    height: 30px;
    background: none;
    border: 1px solid rgb(31, 200, 219);
    border-radius: 10px;
    font-weight: bold;
}
.login-form table button:hover{
    cursor: pointer;
    background-color: rgb(31, 200, 219);
    color: #ffffff;
}

.content-right .menu-top{
    color: #ffffff;
    width: 30%;
    text-align: center;
    margin: auto;
    margin-top: 10px;
}
.menu-top .Login, .menu-top .Register{
    padding: 10px 10px;
    text-decoration: none;
    color: #ffffff;
}
.menu-top .Login:hover, 
.menu-top .Register:hover{
    cursor: pointer;
    color: rgb(31, 200, 219);
}

.content-right .register-form{
    width: 40%;
    min-width: 300px;
    /*background-image: linear-gradient(141deg, rgba(159, 184, 173, 0.8) 0%, rgba(31, 200, 219, 0.7) 50%, rgba(44, 181, 232, 0.6) 71%);*/
    background-color: rgba(255, 255, 255, 0.8);
    padding: 0px 0px;
    margin: auto;
    margin-top: 30%;
    box-shadow: 10px 10px 6px rgba(0, 0, 0, 0.16);

}
.register-form table{
    margin: auto;
    text-align: center;
    border-collapse: separate;
    border-spacing: 0 30px;
}
.register-form table tr:nth-child(1) td:nth-child(1){
    border-bottom: 1px solid #6f6f6f;
}
.register-form table img{
    height: 30px;
    vertical-align: middle;
}
.register-form table input{
    border: none;
    width: 200px;
    height: 2em;
    font-size: 1.1em;
    border-bottom: 1px solid rgb(31, 200, 219);
    background: none;
    padding-left: 10px;
}
.register-form table button{
    width: 80px;
    height: 30px;
    background: none;
    border: 1px solid rgb(31, 200, 219);
    border-radius: 10px;
    font-weight: bold;
}
.register-form table button:hover{
    cursor: pointer;
    background-color: rgb(31, 200, 219);
    color: #ffffff;
}
</style>

<script>
import axios from 'axios';

export default {
   name: 'homepage',
   data(){
       return{
           input:{
               email: "",
               password: "",
               username: ""
           },
           border_color: 'rgb(31, 200, 219)'
       }
   },
   computed:{
       login(){
            let p = this.$route.path
            if(p==='/'){return true}
            else{return false}
       },
       register(){
            let p = this.$route.path
            if(p==='/register'){return true}
            else{return false}
       }
   },
   methods:{
       login_user(){
           let email = this.input.email
           let pass = this.input.password
           if(email != "" && pass!=""){
               axios.get('http://localhost:5000/user/'+ email + '/' + pass).then(({data})=>{
                   if(data=='wrong password' || data=='User not found'){
                       this.border_color = 'red'
                   }
                   else{
                        this.login_log(data.id)
                        data.new_user = false
                        this.$cookie.set('squarenetLogin', JSON.stringify(data) , 5)
                        this.$router.push({name: 'home'})
                   }
                })
           }
           else{
               this.border_color = 'red'
           }
       },
       register_user(){
           let email = this.input.email
           let pass = this.input.password
           let username = this.input.username
           if(email != "" && pass != "" && username != ""){
               axios.post('http://localhost:5000/user', {
                   email: email,
                   password: pass,
                   name: username
               }).then(({data})=>{
                   this.login_log(data.id)
                   data.new_user = true
                   this.$cookie.set('squarenetLogin', JSON.stringify(data) , 5)
                   this.$router.push({name: 'home'})
               })
           }
           else{
               this.border_color = 'red'
           }
       },
       login_log(id_user){
           axios.post('http://localhost:5000/login', {
               user_id: id_user,
           }).then()
       },
   },
}

//Photo by Josh Hild on Unsplash
</script>
