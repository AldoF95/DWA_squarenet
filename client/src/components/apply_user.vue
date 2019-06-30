<template>
    <div class="modal-apply-user">
        <div class="corner"></div>
        <div class="content">
            <ul>
                <li v-for="user in user_data" :key="user.id">
                    <img :src="add_picture(user.gender)"/>
                    {{user.name}}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'modal_user',
    props: ['user_data'],
    methods:{
        add_picture(gender){
            if(gender == 'M'){return require("../assets/profile_male.png")}
            else if(gender == 'F'){return require("../assets/profile_female.png")}
            else{return require("../assets/profile_neutral.png")}
        }
    }
}
</script>

<style>
.modal-apply-user{
    display: inline-block;
    position: absolute;
    width: 200px;
    min-height: 80px;
    max-height: 280px !important;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.corner{
    position: absolute;
    height: 20px;
    width: 20px;
    transform: rotate(45deg);
    background-image: linear-gradient(141deg, rgba(159, 184, 173, 0.8) 0%, rgba(31, 200, 219, 0.7) 51%, rgba(44, 181, 232, 0.6) 75%);
    float: left;
    margin-top: 30px;
    z-index: -1;

}

.modal-apply-user .content{
    height: 100%;
    min-height: 80px;
    max-height: 280px !important;
    width: 190px;
    padding: 0;
    margin: 0;
    float: right;
    background-image: linear-gradient(141deg, rgba(159, 184, 173, 0.8) 0%, rgba(31, 200, 219, 0.7) 51%, rgba(44, 181, 232, 0.6) 75%);
    border-radius: 13px;
    overflow: auto;
}
.modal-apply-user .content ul{
    width: 180px;
    list-style: none;
    padding:0;
    background: none;
}
.modal-apply-user .content ul li{
    margin:0;
    padding-left: 15px;
}
.modal-apply-user .content ul img{
    height: 55px;
    vertical-align: middle;
}
</style>
