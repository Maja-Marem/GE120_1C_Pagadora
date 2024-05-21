import React from 'react' //to create a state
import { Picker } from '@react-native-picker/picker'; //import from react native
import { StyleSheet, Text, TextInput, View, Button } from 'react-native'; //dito lahat ng pwedeng components na ilagay

export default function App() {

  const [outputValue, setOutputValue] = React.useState('---'); //anytime you type something, ayun yung gagawin ng setOutput //INITIALIZATION
  const [inputValue, setInputValue] = React.useState('Input value here..'); //INITIALIZATION
  const [inputCase, setInputCase] = React.useState("Select Case"); //INITIALIZATION
  const blurhash =
  '|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj['; //INITIALIZATION

  function convertValue(value) {  //CREATING A DD-DMS AND DMS-DD CONVERSION FUNCTION
      /*
      Compute for the bearing of a given angle.

      Input:
      azimuth - float

      Output:
      bearing - string
      */
      
      if (inputCase == "1") {
        var degrees = Math.floor(value)
        var minutes = Math.floor((value-degrees)*60)
        var seconds = Math.round((value-degrees-(minutes/60))*3600)

        var output = degrees.toString().concat("-", minutes.toString(), "-", seconds.toString())

        setOutputValue(output)
      }
      else {
        var elements = value.split("-")
        var output = parseFloat(elements[0]) + parseFloat(elements[1])/60 + parseFloat(elements [2])/3600
        setOutputValue(output)
      }
  }

  return (
    <View style={styles.box}>
      <View style={styles.box1}>
        <Text style={styles.titleText}> WELCOME TO DMS-DD CONVERTER APP </Text>
      </View>
      
      <View style={styles.box2}> 
        <View style={styles.box21}>
          <Text>Input Case</Text>
          <Picker
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="DD to DMS" values="1" />
            <Picker.Item label="DMS to DD" values="2" />
          </Picker>
        </View>
      
        <View style={styles.box22}>
          <TextInput
            style={styles.input}
            onChangeText={setInputValue}
            value={inputValue}
          />
          <Button
            title="Convert"
            onPress={() => convertValue(inputValue)}
          />
        </View>  
      </View>

      <View style={styles.box3}>
        <Text style={styles.titleText}> Output: </Text>
        <Text style={styles.titleText}> {outputValue} </Text>
      </View>
    </View>
  );
}

//INITIALIZATION
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  box1: {
    width: '100%', 
    height: '10%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  box2: {
    width: '100%', 
    height: '25%', 
    alignItems: 'center', 
    justifyContent: 'center',      
    padding: 10  
  },
  box21: {
    flexDirection: 'column',
    width: '100%',
    height: '50%',   
    padding: 10
  },
  box22: {
    flex: 1,
    width: '100%',
    height: '50%',
  },
  box3: {
    width: '100%', 
    height: '25%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  box4: {
    width: '100%', 
    height: '40%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  titleText: {
    fontSize: 24,
    fontWeight: 'bold', 
    color: 'black'
  },
  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'black'
  }
});


