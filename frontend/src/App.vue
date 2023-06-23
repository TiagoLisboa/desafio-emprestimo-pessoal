<script setup lang="ts">
    import axios from 'axios'
    import { ref } from 'vue'

    const proposalFields = ref([]);
    const fieldRefs = ref([])


    const headers = {
        'Sec-Fetch-Site': 'same-origin'
    };
    axios
        .get('http://localhost:1339/api/api/proposal_fields', headers)
        .then(response => {proposalFields.value = response.data});

</script>

<template>
    <main>
        <div v-for="field in proposalFields" ref="fieldRefs">
            <label :for="field.id">
                {{ field.name }}
            </label>
            <input v-if="field.field_type == 'string'" type="text" :name="field.name" :id="field.id" />
            <input v-if="field.field_type == 'numeric'" type="number" :name="field.name" :id="field.id" />
            <input v-if="field.field_type == 'integer'" type="number" step="1" :name="field.name" :id="field.id" />
            <input v-if="field.field_type == 'boolean'" type="checkbox" :name="field.name" :id="field.id" />
        </div>
    </main>
</template>

<style scoped></style>
