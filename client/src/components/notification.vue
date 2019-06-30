<template>
    <div class="modal-notification">
        <div class="square"></div>
        <div class="body">
            <ul>
                <li>
                    <table>
                        <tr>
                            <td><img src="../assets/profile_neutral.png"/></td>
                            <td>Aldo has applied to your event</td>
                        </tr>
                        <tr>
                            <td colspan="2" >
                                <button>Accept apply</button>
                                <button>Decline apply</button>
                            </td>
                        </tr>
                    </table>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'notify',
    props: ['user_id']
}
</script>

<style>
.modal-notification{
    display: inline-block;
    position: absolute;
    width: 350px;
    min-height: 80px;
    max-height: 380px !important;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.square{
    position: absolute;
    height: 25px;
    width: 25px;
    top: 0;
    right: 30px;
    transform: rotate(45deg);
    background-image: linear-gradient(145deg, rgb(114, 133, 134) 0%, rgb(19, 123, 134) 51%, rgb(17, 93, 121) 75%);
    z-index: -1;

}

.modal-notification .body{
    min-height: 80px;
    max-height: 350px !important;
    width: 100%;
    padding: 15px 0;
    margin: 0;
    margin-top: 10px;
    background-image: linear-gradient(141deg, rgb(114, 133, 134) 0%, rgb(19, 123, 134) 51%, rgb(17, 93, 121) 75%);
    border-radius: 13px;
    overflow: auto;
}
.modal-notification .body ul{
    width: 300px;
    margin: auto;
    list-style: none;
    padding: 0;
    background: none;
}
.modal-notification .body ul li{
    color: #ffffff;
    margin:0;
    border-bottom: 1px solid #ffffff;
}
.modal-notification .body ul img{
    height: 55px;
    vertical-align: middle;
}
.modal-notification .body ul button{
    height: 28px;
    width: 110px;
    background: none;
    border: 1px solid #ffffff;
    border-radius: 14px;
    color: #ffffff;
    margin: 2px 5px;
    vertical-align: middle;
}
.modal-notification .body ul table{
    width: 100%;
}
.modal-notification .body ul table tr:nth-child(2){
    text-align: center;
}
</style>
