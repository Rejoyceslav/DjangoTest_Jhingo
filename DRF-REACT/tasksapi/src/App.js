import React from 'react';
class connectionExample extends React.Component {
  componentDidMount() {
    const apiUrl = 'http://127.0.0.1:8000/api/tasks/';
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => console.log(data));
  }
  render() {
    return <div>Example connection</div>;
  }
}

export default connectionExample;
