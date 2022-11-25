<style>
.input-text {
    color: black;
    text-transform: uppercase;
    padding-left: 4px;
    border-radius: 6px;
}
</style>

<script>
export default {
    name: 'CesarCipher',
    props: {
        modelValue: [String, Number]
    },
    methods: {
        updateValue(event){
            this.$emit('update:modelValue', event.target.value)
        }
    }
}
// const props = defineProps({
//     messageCiphered: {
//         default: 'abc'
//     },
//     message: {
//         default: 'teste'
//     },
//     defaultKey: {
//         default: '2'
//     }
// })

// function printEvent(event) {
//     key = event.target.value.replace(/[^0-9]/g, '')
//     // key = e.target.value.replace(/[^0-9]/g, '')
// }

</script>

<template>
    <div>
        Mensagem: <input class="input-text" :value="message" maxlength="12" />
    </div>
    <div style="margin-top:10px">
        Chave: <input class="input-text" :value="modelValue" style="width:30px" maxlength="1" @input="updateValue" />
    </div>
    <div>
        <span>{{ modelValue }}</span>
    </div>
</template>