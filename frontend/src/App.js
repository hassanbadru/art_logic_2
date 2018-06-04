import React, { Component } from 'react';
import './css/App.css';

class App extends Component {
  constructor(props){
    super(props)
    this.state = {operation: 'encoding', user_input: '', file_upload: false, result: '', part: 2}
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


            {
              (this.state.part === 1) ? (
                <Part1
                  toEncode={() => this.setState({operation: 'encoding'})}
                  toDecode={() => this.setState({operation: 'decoding'})}
                  user_input={(user_input) => this.setState({user_input})}
                  currentOperation={this.state.operation}
                  toUpload={() => this.setState({file_upload: !this.state.file_upload})}
                  file_upload={this.state.file_upload}
                  get_result={() => this.setState({result: window.result})}

                  currentOperation={this.state.operation}
                  user_input={this.state.user_input}
                  result={this.state.result}
                />
              ) : (
                <Part2 />
              )


            }


            </div>
        </div>
      </div>

    );
  }
}


// const Part2 = (props) => {
//
// }


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

const Part1 = (props) => {
  return (
    <div className={'row'}>
      <UserInput
        toEncode={props.toEncode}
        toDecode={props.toDecode}
        user_input={props.user_input}
        currentOperation={props.currentOperation}
        toUpload={props.toUpload}
        file_upload={props.file_upload}
        get_result={props.get_result}
      />

      <ResultDisplay
        currentOperation={props.operation}
        user_input={props.user_input}
        result={props.result}
      />
    </div>
  )
}

const Part2 = (props) => {
  return (
    <div style={{backgroundColor: '#fff', paddingTop: 30}}>
      <h4>Entire desired instruction</h4>
      <br />
      <UserInput2 />
    </div>
  )
}


const UserInput2 = (props) => {

  return (

    <div className="form">
      <form action="">


        <input
          type="text"
          placeholder='Instruction'
          name="to_compute"

        />

        <button type="submit"> Compute</button>

      </form>

      {/* <a href={window.MEDIA_URL + '/ConvertedData.txt'}>
        <i className={'message'} className="fas fa-download" > {'download ConvertedData.txt'} </i>
      </a> */}

    </div>
  )
}



export default App;
