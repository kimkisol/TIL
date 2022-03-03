import React, { Component } from 'react';

class PhoneForm extends Component {

  state = {
    name: '',
    phone: '',
  }

  handleChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  handleSubmit = (event) => {
    event.preventDefault()
    this.props.onCreate(this.state)
    this.setState({
      name: '',
      phone: '',
    })
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <h1>Phone Form</h1>
        <input 
          name="name"
          placeholder="이름" 
          onChange={this.handleChange} 
          value={this.state.name} 
        />
        <input 
          name="phone"
          placeholder="전화번호" 
          onChange={this.handleChange} 
          value={this.state.phone} 
        />
        <button type="submit">등록</button>
      </form>
    );
  }
}

export default PhoneForm;