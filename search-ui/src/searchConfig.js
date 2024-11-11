import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

const connector = new ElasticsearchAPIConnector({
  host: "http://localhost:9200",
  index: "cv-transcriptions",
});

export const searchConfig = {
  apiConnector: connector,
  searchQuery: {
    search_fields: {
      generated_text: {},
      duration: {},
      age: {},
      gender: {},
      accent: {},
    },
    result_fields: {
      generated_text: {},
      duration: {},
      age: { raw: {} },
      gender: { raw: {} },
      accent: { raw: {} },
    },
  },
};
