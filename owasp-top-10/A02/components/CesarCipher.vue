<style>
.input-text {
    color: black;
    padding-left: 4px;
    border-radius: 6px;
}

.alpha-table td {
    font-size: 10px;
    padding: 1px !important;
}
</style>

<script>
export default {
    data() {
        return {
            message: '',
            key: '',
            ciphered: ''
        }
    },
    methods: {
        updateCiphered(e) {
            this.message = this.message.toUpperCase().replace(/[^A-Z ]/g, '')
            const keyInt = parseInt(this.key)
            if (isNaN(keyInt) || keyInt > 25)
                return ''

            const alphabetic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            let result = ''

            for (let c of this.message) {
                let idx = alphabetic.indexOf(c)

                if (idx === -1) {
                    result += ' '
                    continue
                }

                idx = idx + keyInt
                if (idx > 25)
                    idx = idx - 26
                result += alphabetic[idx]
            }

            this.ciphered = result
        }
    }
}

</script>

<template>
    <div>
        Mensagem: <input class="input-text" v-model="message" maxlength="12" />
    </div>
    <div style="margin-top:10px">
        Chave Numérica: <input class="input-text" v-model="key" style="width:30px" maxlength="2" />
    </div>
    <button style="font-size:10px;border: 1px solid white;padding:4px;border-radius:4px;margin:14px 0px"
        @click="updateCiphered">ATUALIZAR</button>
    <div>
        Cifrado: <span style="color:green">{{ ciphered }}</span>
    </div>
    <br />
    <table class="alpha-table">
        <tbody>
            <tr>
                <td>A</td>
                <td>B</td>
                <td>C</td>
                <td>D</td>
                <td>E</td>
                <td>F</td>
                <td>G</td>
                <td>H</td>
                <td>I</td>
                <td>J</td>
                <td>K</td>
                <td>L</td>
                <td>M</td>
                <td>N</td>
                <td>O</td>
                <td>P</td>
                <td>Q</td>
                <td>R</td>
                <td>S</td>
                <td>T</td>
                <td>U</td>
                <td>V</td>
                <td>W</td>
                <td>X</td>
                <td>Y</td>
                <td>Z</td>
            </tr>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
                <td>4</td>
                <td>5</td>
                <td>6</td>
                <td>7</td>
                <td>8</td>
                <td>9</td>
                <td>10</td>
                <td>11</td>
                <td>12</td>
                <td>13</td>
                <td>14</td>
                <td>15</td>
                <td>16</td>
                <td>17</td>
                <td>18</td>
                <td>19</td>
                <td>20</td>
                <td>21</td>
                <td>22</td>
                <td>23</td>
                <td>24</td>
                <td>25</td>
                <td>26</td>
            </tr>
        </tbody>
    </table>
</template>