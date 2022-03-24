import logo from './logo.svg';
import { useState } from 'react';
import './App.css';

function Header({title, onClick}) {
  return (
    <header>
      <h1><a href='/' onClick={onClick}>{title}</a></h1>
    </header>
  )
}

function Nav({ topics, onClick }) {
  const lis = []
  for (let i=0; i<topics.length; i++) {
    let t = topics[i]
    lis.push(<li key={t.id}>
      <a href={'/read/'+t.id} onClick={event=>{
        event.preventDefault()
        onClick(t.id)
      }}>{t.title}</a>
    </li>
  )}

  return (
  <nav>
    <ol>
      {lis}
      {/* <li><a href='/read/1'>html</a></li>
      <li><a href='/read/2'>css</a></li>
      <li><a href='/read/3'>js</a></li> */}
    </ol>
  </nav>
  )
}

function Article({ title, body }) {
  return (
    <article>
      <h2>{title}</h2>
      {body}
    </article>
  )
}

function Create({onCreate}) {
  return (
    <article>
      <h2>Create</h2>
      <form action="" onSubmit={event=>{
        event.preventDefault()
        const title = event.target.title.value
        const body = event.target.body.value
        onCreate(title, body)
      }}>
        <input type="text" name='title' placeholder='title' /><br />
        <textarea name="body" id="" cols="30" rows="10" placeholder='body'></textarea><br />
        <input type="submit" value="create" />
      </form>
    </article>
  )
}

function Update({originTitle, originBody, onUpdate}) {
  const [title, setTitle] = useState(originTitle)
  const [body, setBody] = useState(originBody)
  return (
    <article>
      <h2>Update</h2>
      <form action="" onSubmit={event=>{
        event.preventDefault()
        const updatedTitle = event.target.title.value
        const updatedBody = event.target.body.value
        onUpdate(updatedTitle, updatedBody)
      }}>
        <input type="text" name='title' placeholder='title' value={title} onChange={(event)=>{
          setTitle(event.target.value)
        }} /><br />
        <textarea name="body" id="" cols="30" rows="10" placeholder='body' value={body} onChange={(event)=>{
          setBody(event.target.value)
        }}></textarea><br />
        <input type="submit" value="update" />
      </form>
    </article>
  )
}

function App() {
  const [mode, setMode] = useState('WELCOME')
  const [id, setId] = useState(null)
  const [nextId, setNextId] = useState(3)
  const [topics, setTopics] = useState([
    {id: 0, title: 'html', body: 'html is ...'},
    {id: 1, title: 'css', body: 'css is ...'},
    {id: 2, title: 'js', body: 'js is ...'}
  ])
  let content = null
  if(mode === 'WELCOME'){
    content = <Article title="Welcome!" body="Hello, React!" />
  } else if(mode === 'READ'){
    let title = topics[id].title;
    let body = topics[id].body;
    content = (
    <>
      <Article title={title} body={body} />
      <a href={"/"+id+"/update"} onClick={function(event){
        event.preventDefault()
        setMode('UPDATE')
      }}>Update</a><br></br>
      <a href="/" onClick={function(event){
        event.preventDefault()
        setTopics(topics.filter(topic => topic.id !== id))
        setId(null)
        setMode('WELCOME')
      }}>Delete</a><br></br>
    </>
  )
  } else if(mode === 'CREATE'){
    console.log('create')
    content = <Create onCreate={(title, body) => {
      const newTopics = [...topics, {id:nextId, title, body}]
      setTopics(newTopics)
      setId(nextId)
      setNextId(nextId + 1)
      setMode('READ')
    }} />
  } else if(mode === 'UPDATE'){
    function onUpdate (title, body){
      const updatedTopics = [...topics]
      updatedTopics[id] = {id, title, body}
      setTopics(updatedTopics)
      setMode('READ')
    }
    content = <Update originTitle={topics[id].title} originBody={topics[id].body} onUpdate={onUpdate} />
  }

  return (
    <div className="App">
      Hello React
      <Header title="React" onClick={function(){
        setMode('WELCOME');
      }} />
      <Nav topics={topics} onClick={(id)=>{
        setMode('READ');
        setId(id)
        console.log(typeof(id))
      }}/>
      {content}
      <a href="/create" onClick={function(event){
        event.preventDefault();
        setMode('CREATE');
      }}>Create</a>
    </div>
  );
}

export default App;
