import React from "react";
import {
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging
} from "@elastic/react-search-ui";
import { searchConfig } from "./searchConfig";
import "@elastic/react-search-ui-views/lib/styles/styles.css";

function App() {
  return (
    <SearchProvider config={searchConfig}>
      <div className="App">
        <h1>Search UI</h1>
        <SearchBox autocompleteSuggestions={true} />
        <PagingInfo />
        <ResultsPerPage />
        <Results
          titleField="generated_text"
          urlField="filename"
          shouldTrackClickThrough={true}
          resultView={({ result }) => (
            <div>
              <h3>{result.generated_text}</h3>
              <p>Duration: {result.duration}</p>
              <p>Age: {result.age.raw}</p>
              <p>Gender: {result.gender.raw}</p>
              <p>Accent: {result.accent.raw}</p>
            </div>
          )}
        />
        <Paging />
      </div>
    </SearchProvider>
  );
}

export default App;
