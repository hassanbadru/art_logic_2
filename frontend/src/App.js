import React, { Component } from 'react';
import './css/App.css';

class App extends Component {
  constructor(props){
    super(props)
    this.state = {operation: 'encoding', user_input: '', file_upload: false, result: ''}
  }


    // componentWillMount(){
    //     fetch('api/art_logic_app/').then(res => res.json).then(data => this.setState(data))
    //     console.log(props.data)
    // }

  render() {

    return (
      <div id={"intro"}>
        <div className={"intro-body"}>
          <div className={"container"}>

            <div className={"row"}>
              <div className={"col-md-12"}>
                <h1>ART +<span className={"brand-heading"}> LOGIC</span></h1>
                <p className={"intro-text"}>Use this app to encode and decode data...</p>
              </div>
             </div>

             <div className={'row'}>

               <UserInput
                 toEncode={() => this.setState({operation: 'encoding'})}
                 toDecode={() => this.setState({operation: 'decoding'})}
                 user_input={(user_input) => this.setState({user_input})}
                 currentOperation={this.state.operation}
                 toUpload={() => this.setState({file_upload: !this.state.file_upload})}
                 file_upload={this.state.file_upload}
                 get_result={() => this.setState({result: window.result})}
               />

               <ResultDisplay
                 currentOperation={this.state.operation}
                 user_input={this.state.user_input}
                 result={this.state.result}
                />
             </div>



            </div>
        </div>
      </div>

    );
  }
}

export default App;

const UserInput = (props) => {

  let encodingStatus = props.currentOperation === 'encoding'

  return (

    <div className={"form"}>
        <form action="">
          <h4>Select an operation</h4>
          <span className={'message'}>

              <div>
                <label className={"radio-inline message"}>&nbsp;<input type="radio" name="encode" onChange={props.toEncode} checked={encodingStatus} />Encode</label>
                <label className={"radio-inline message"}>&nbsp;<input type="radio" name="decode" onChange={props.toDecode} checked={!encodingStatus}/>Decode</label>
              </div>

          </span>

          <br/>
          {
            (props.file_upload) ? (
                    <div>
                      <input
                        type="file"
                        name="file_compute"
                      />

                      <p style={{color: '#000'}}>Prefer to type in? Use the<a onClick={props.toUpload} href="#" style={{color: 'orange'}}> Text Box</a></p>
                      <button>Compute</button>
                    </div>
                  ) : (
                    <div>
                      <input
                        type="text"
                        placeholder={(encodingStatus) ? 'Enter Decimal Value' : 'Enter Hexadecimal Value'}
                        name="to_compute"
                        onChange={(e) => {
                          props.user_input(e.target.value)
                          console.log(e.target.value)
                        }}
                      />
                      {/* <p style={{color: '#000'}}>Have a text file? <a onClick={props.toUpload} href="#" style={{color: 'orange'}}>Upload</a> instead</p> */}

                      <button type="submit" onClick={props.get_result}> Compute</button>
                    </div>
                  )
          }

          <br/>

        </form>

        <a href={window.MEDIA_URL + '/ConvertedData.txt'}>
          <i className={'message'} className="fas fa-download" > {'download ConvertedData.txt'} </i>
        </a>

      </div>
  )
}

const ResultDisplay = (props) => {

  // console.log(window.result)

  return (
    <div className={"result_view"}>
        <h4 style={{color: '#000'}}>
          {(props.currentOperation == 'encoding') ? 'ENCODING' : 'DECODING'}
        </h4>
        <p style={{color: '#000'}}> {(props.currentOperation === 'encoding') ? '(dec to hex)' : '(hex to dec)'}</p>
        <hr style={{width: '100%'}}></hr>

        {/* {(props.result) ? () : null} */}

        {
          (window.result) ? (
            (window.result.length <= 6) ? (
            <div>
              <h3 style={{color: '#000'}}>RESULTS</h3>
              <p style={{color: '#000'}}>{window.result}</p>
            </div>
            ) : (
              <i style={{color: 'red'}}>{'Error: ' + window.result}</i>
            )
          ) : null
        }

        {/* <p style={{color: '#000'}}>Download <a href="#" style={{color: 'orange'}}>Text File</a> of RESULT</p> */}

    </div>
  )
}

//
// <div className="App">
//   <header className="App-header">
//     <img src={logo} className="App-logo" alt="logo" />
//     <h1 className="App-title">Welcome to React</h1>
//   </header>
//   <p className="App-intro">
//     To get started, edit <code>src/App.js</code> and save to reload.
//   </p>
// </div>
