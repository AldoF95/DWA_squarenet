<template>
    <div class="button-post-search">
          <table class="buttons">
              <tr>
                  <td><button @click="hidden = false"><img src="../assets/post.png"/>Post activity</button></td>
                  <td><button><img src="../assets/search.png"/>Search activity</button></td>
              </tr>
            
          </table>
            <div class="post-new" v-if="!hidden">
                
                <form>
                    <button class="exit-new-post" @click="hidden=!hidden"/>
                    <table>
                        <tr>
                            <td>
                                <input type="text" name="post-title" placeholder="Activity title" v-model="new_post.title"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <table class="post-section">
                                    <tr>
                                        <td><timeselector v-model="time_s" :placeholder="'Select time'" :displayFormat="'HH:mm'"></timeselector></td>
                                        <td><img src="../assets/time_w.png"/></td>
                                        <td><input type="text" name="post-location" placeholder="Location" v-model="new_post.location"/></td>
                                        <td><img src="../assets/location_w.png"/></td>
                                    </tr>
                                    <tr>
                                        <td><v-date-picker v-model="date"  /></td>
                                        <td><img src="../assets/calendar_w.png"/></td>
                                        <td><input type="text" name="post-people" placeholder="People needed" v-model="new_post.people"/></td>
                                        <td><img src="../assets/people_w.png"/></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr class="description-row">
                            <td>
                                <img src="../assets/info.png"/>
                                <textarea maxlength="230" placeholder="Description" name="post-description" v-model="new_post.description">
                                </textarea>
                            </td>
                        </tr>
                        <tr>
                            <td><select v-model="new_post.tag"><option v-for="tag in tags" :key="tag.id" :value="tag.id">{{tag.name}}</option></select></td>
                        </tr>
                        <tr>
                            <td><button @click.prevent="create_post()">Post It <img src="../assets/post.png"/></button></td>
                        </tr>
                    </table>
                    
                </form>
            </div>
            <div class="post-search"></div>
    </div>
</template>

<style>
.button-post-search .buttons{
    margin: auto;
    height: 35px;
    padding-top: 20px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.button-post-search .buttons button{
    height: 35px;
    width: 250px;
    background: none;
    border: 2px solid #012477;
    border-radius: 17.5px;
    text-align: center;
    font-size: 1.05em;
    font-weight: bold;

}
.button-post-search .buttons button:hover{
    cursor: pointer;
}
.button-post-search .buttons button:nth-child(1){
    margin-right: 20px;
}
.button-post-search .buttons button:nth-child(2){
    margin-left: 20px;
}
.button-post-search .buttons img{
    height: 100%;
    padding-right: 5px;
    vertical-align: middle;
}

.post-new{
    position: absolute;
    top: 50px;
    left: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(114, 135, 143, 0.9);
}

.post-new form{
    z-index: 1;
    height: 500px;
    width: 370px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    border-radius: 100px 13px 100px 13px;
    border: 1px solid #707070;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-size: 1.2em;
    box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.16);
    margin-right: 20px;
    margin-top: 30px;
}
.post-new form .exit-new-post{
    width: 30px;
    height: 30px;
    position: absolute;
    right: -10px;
    top: -10px;
    background-color: #ffffff;
    background-image: url('../assets/x.png');
    background-size: cover;
    background-position: center;
    border: 1px solid #707070;
    border-radius: 50%;

}
.post-new form .exit-new-post:hover{
    cursor: pointer;
    border: 1.5px solid #012477;
}
.post-new form table{
    text-align: center;
    margin: auto;
    height: 100%;
}
.post-new form .post-section{
    margin: 0;
    padding: 5px;
    background-color: #012477;
    border-radius: 15px;
    height: 130px;
}
.post-new form .post-section input{
    color: #ffffff;
    margin-left: 5px;
    width: 110px;
    background: none;
    border: none;
    border-bottom: 1px solid #ffffff;
}
.post-new form table img{
    margin: 0;
    padding: 0;
    height: 30px;
}
.post-new form>table>tr:nth-child(1)>td input:nth-child(1){
    width: 200px;
    height: 32px;
    background: none;
    border: 1px solid #707070;
    border-radius: 11px;
    padding-left: 5px;
}
.post-new form table .description-row textarea{
    resize: none;
    height: 140px;
    width: 281px;
    border: 1px solid #707070;
    border-radius: 11px;
    padding-left: 30px;
}
.post-new form table .description-row img{
    position: absolute;
}
.post-new form table select{
    width: 200px;
    height: 30px;
    border: 1px solid #707070;
    border-radius: 11px;
    background: none;
}
.post-new form table button{
    width: 150px;
    height: 30px;
    border: 2px solid #012477;
    border-radius: 15px;
    text-align: center;
    font-weight: bold;
    background: none;
}
.post-new form table button:hover{
    cursor: pointer;
    background-color: #012477;
    color: #ffffff;
}
.post-new form table button img{
    height: 26px;
    display: inherit;
    vertical-align: middle;
    padding-left: 5px;
}

</style>

<script>
import axios from 'axios'
import timeselector from 'vue-timeselector'
export default {
    name: 'new_post_search',
    props: ['logged_user'],
    components:{
        timeselector
    },
    data(){
        return{
            hidden: true,
            date: new Date(),
            time_s: new Date(),
            new_post:{
                title: "",
                time : "",
                location: "",
                people: "",
                description: "",
                tag: [],
                user_id: this.logged_user.id
            },
            tags: null
        }
        
    },
    methods:{
        //"7/3/2019 00:00:00"
        create_post(){
            let D = String(this.date.getDate())
            let M = String(this.date.getMonth())
            let Y = String(this.date.getFullYear())
            let h = (this.time_s.getHours()<10?'0':'')+ String(this.time_s.getHours())
            let m = (this.time_s.getMinutes()<10?'0':'')+String(this.time_s.getMinutes())
            let s = (this.time_s.getSeconds()<10?'0':'')+String(this.time_s.getSeconds())

            let fullDate = M+"/"+D+"/"+Y+" "+h+":"+m+":"+s
            this.new_post.time = fullDate

            console.log(this.new_post)

            axios.post('http://localhost:5000/posts', {
                title: this.new_post.title,
                body: this.new_post.description,
                time_posted: "",
                user_id: this.new_post.user_id,
                due_time: this.new_post.time,
                location: this.new_post.location,
                tag_id: this.new_post.tag,
                need_users: parseInt(this.new_post.people)
            }).then(({data})=>{
                console.log(data)
                this.$router.push({name: 'home'})
            })
            
        },
        get_tags(){
         axios.get('http://localhost:5000/tags').then(({data})=>{
              this.tags = data.data
          }) 
        }
    },
    beforeMount(){
        this.get_tags()
    }
}
</script>
