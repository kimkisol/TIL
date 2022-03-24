import logo from './logo.svg';
import './App.css';

function App() {
  const name = "Kisol"
  const naver = {
    name: "naver",
    url: "https://naver.com",
  }
  return (
    <div className="App">
      <h1
        style={{
          color: 'white',
          backgroundColor: 'green',
        }}
      >
        Welcome {name} {30-1}
      </h1>
      <a href={naver.url}>{naver.name}</a>
    </div>
  );
}

export default App;
