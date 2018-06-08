import React, { Component } from 'react';
import './css/App.css';

import {XYPlot, XAxis, YAxis, HorizontalGridLines, VerticalGridLines, LineSeries} from 'react-vis';


class App extends Component {
  constructor(props){
    super(props)
    this.state = {operation: 'encoding', user_input: '', file_upload: false, result: '', part: 2}
  }

  render() {

    return (
      <div id="intro">
        <div className="intro-body">
          <div className="container">

            <div className={"row"}>
              <div className="col-md-12">
                <h1>ART +<span className="brand-heading"> LOGIC</span></h1>
                <p className="intro-text">Use this app to encode and decode data...</p>
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
        {(props.currentOperation === 'encoding') ? 'ENCODING' : 'DECODING'}
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

// style={{height: 'auto', width: '100%'}}

const UserInput2 = (props) => {

  return (

    <div className="form">
      <br/>
      <h4>Entire desired instruction</h4>
      <br />

      <form action="">
        <input
          type="text"
          placeholder='Instruction'
          name="instruction_string"
        />

        <button type="submit">Compute</button>
      </form>
    </div>
  )
}


const ResultDisplay2 = (props) => {

  let instruction_stream = props.instruction_stream
  let all_instructions = []
  let color

  // console.log(instruction_stream)
  if (instruction_stream){

    let l = Object.keys(instruction_stream).length

    // let x=0, y=0, xx=0, yy=0
    let pen_down = false;

    for (var i =0; i < l; i++){
      let key = Object.keys(instruction_stream[i])[0]



      // SELECT COLOR
      if (key === 'CO'){
        let color_array = instruction_stream[i][key]
        color = "rgba(" + color_array[0] + ", " + color_array[1] + ", " + color_array[2] + ", " + color_array[3] + ")"
        // console.log(color)
      }


      // PEN LOGIC
      // if (instruction_stream[i] === 'PEN UP'){
      //   pen_down = false
      //   // console.log("PEN:", pen_down)
      // }else if (instruction_stream[i] === 'PEN DOWN'){
      //   pen_down = true
      //   // console.log("PEN UP:", pen_down)
      // }



      // DRAW LOGIC
      // if (key === 'MV'){
      //   if (pen_down){
      //     //move (x, y)
      //     x += instruction_stream[i][key][0]
      //     y += instruction_stream[i][key][1]
      //
      //
      //     // WHEN EXCEEDING BOUNDARY
      //
      //     //pen up - out of boundary
      //
      //
      //     // leave pen at border if out of bounds
      //     if (x > 8191){
      //
      //       pen_down = false //pen down
      //       xx = 8191 //set to boundary (x)
      //
      //       console.log("x > 8191")
      //
      //     } else if (x < -8192){
      //
      //       pen_down = false //pen down
      //       xx = -8192 //set to boundary (x)
      //       console.log("x < -8192")
      //
      //     } else {
      //
      //       pen_down = true //pen up
      //       xx = x // last drawn x
      //
      //       console.log("x normal")
      //     }
      //
      //     if (y > 8191){
      //
      //       pen_down = false //pen down
      //       yy = 8191 //set to boundary (y)
      //
      //       console.log("y > 8191")
      //
      //     } else if (y < -8192){
      //
      //       pen_down = false //pen down
      //       yy = -8192 //set to boundary (y)
      //       console.log("y < -8192")
      //
      //     } else {
      //
      //       pen_down = true //pen up
      //       yy = y // last drawn y
      //       console.log("y normal")
      //
      //     }
      //
      //     instruction_stream[i][key] = [xx, yy]
      //
      //
      //
      //   } else if (!(x > 8191 && x < -8192) || !(y > 8191 && y < -8192)) {
      //     // if pen up but still within boundary
      //     // xx = x
      //     // yy = y
      //     // xx = instruction_stream[i][key][0]
      //     // yy = instruction_stream[i][key][1]
      //   }
      //       instruction_stream[i][key] = [xx, yy]
      //       console.log(instruction_stream[i][key])
      // }


      all_instructions.push(instruction_stream[i])
    }



    // console.log(all_instructions)

  }



  return (
    <div className="col-md-12" style={{backgroundColor: '#eee'}}>

      <br />
      <br />
      <a href="/"> Back</a>
      <br />
      <br />


      <h5 style={{color: '#000'}}>PART #2 RESULTS</h5>
      <hr />

      <div className="row">

        <div className="col-md-5">
          <p style={{color: '#000'}}>DECODED POSITIONS</p>

          <div style={{overflowY: 'auto', height: 300, width: '100%'}}>
            <ul>
              { (instruction_stream) ?
                all_instructions.map((instruction, i) => {
                  let key = Object.keys(instruction)[0]
                  return (
                    <li key={i}>
                      <h5 style={{color: '#000'}}>{(typeof instruction === 'object') ? key + ": " + instruction[key] : instruction}</h5>
                    </li>
                  )
                }) : null
              }
            </ul>
          </div>

        </div>

        <div className="col-md-7" style={{backgroundColor: '#fff', height: 300, padding: 5}}>
          <p style={{color: '#000'}}>GRAPH</p>
          <PlotGraph color={(color) ? color : "black"} all_instructions={all_instructions} />
        </div>

      </div>

    </div>
  )
}




// PART 2
class Part2 extends Component {

  render(){

    let instruction_stream = window.instruction_stream

      if (typeof instruction_stream !== 'string') {
        return <ResultDisplay2 instruction_stream={instruction_stream} />
      } else {
        return <UserInput2 instruction_stream={instruction_stream} />
      }


  }
}

const PlotGraph = (props) => {
  let coordinates = [];

  (props.all_instructions) ?
    props.all_instructions.map((instruction, i) => {
      if (Object.keys(instruction)[0] === 'MV'){
        // console.log(instruction['MV'])
        coordinates.push(instruction['MV'])
      }
      // coordinates.push(instruction['MV'])

    }) : null

    console.log(coordinates)


  return (
  <div style={{marginHorizontal: 20}}>
    <XYPlot
      width={250}
      height={250}
      getX={d => d[0]}
      getY={d => d[1]}>

      {/* <VerticalGridLines /> */}
      <HorizontalGridLines />

      <LineSeries
        color={props.color}
        data={(coordinates)? coordinates : [[1, 1],[3, 4],[3, 7]]}
        style={{line:{stroke: 'white'}, strokeWidth: 5}}
      />

      <XAxis />
      <YAxis />
    </XYPlot>
  </div>
  )
}
// strokeLinejoin: "round"
// const divStyle={
//   overflowY: 'auto',
//   // border:'1px solid red',
//   width:'100%',
//   height:'auto',
//   position:'relative',
//   backgroundColor: '#eee',
//   marginBottom: 15
// };



export default App;
