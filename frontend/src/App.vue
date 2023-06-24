<script setup lang="ts">
    import axios from 'axios';
    import { ref } from 'vue';

    const proposalFields = ref([]);
    const fieldRefs = ref([]);
    const answers = ref({})
    let defaultAnswers = {}

    const headers = {
        'Sec-Fetch-Site': 'same-origin'
    };


    axios
        .get('http://localhost:1339/api/api/proposal_fields', headers)
        .then(response => {
            function getDefaultValue(type) {
                switch (type) {
                    case "boolean":
                        return false;
                    case "numeric":
                    case "integer":
                        return 0;
                    default:
                        return "";
                }
            }
            proposalFields.value = response.data;

            console.log(defaultAnswers)
            answers.value = defaultAnswers
        });

    function onSubmit(e) {
        e.preventDefault();

        axios
            .post('http://localhost:1339/api/api/proposals', answers.value)
            .then(response => {answers.value = defaultAnswers});
    }

</script>

<template>
    <main>
        <form @submit="onSubmit">
            <div v-for="field in proposalFields" ref="fieldRefs">
                <label :for="field.id">
                    {{ field.name }}
                </label>
                <input v-if="field.field_type == 'string'" type="text" v-model="answers[field.name]" :id="field.id" />
                <input v-if="field.field_type == 'numeric'" type="number" v-model="answers[field.name]" :id="field.id" />
                <input v-if="field.field_type == 'integer'" type="number" step="1" v-model="answers[field.name]" :id="field.id" />
                <input v-if="field.field_type == 'boolean'" type="checkbox" v-model="answers[field.name]" :id="field.id" />
            </div>
            <button>Submit</button>
        </form>
    </main>
</template>

<style scoped></style>
