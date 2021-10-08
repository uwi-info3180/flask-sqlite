class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            userButton: document.querySelector('.chatbox__messages')
        }
        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton, userButton} = this.args;
        window.value=0;
        window.myvalue=0;
        window.margq=0;
        openButton.addEventListener('click', () => this.toggleState(chatBox))
        sendButton.addEventListener('click', () => this.onSendButton(chatBox))
        userButton.addEventListener('click', () => this.newUser(chatBox))
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    newUser(chatbox) {
      if(window.myvalue===0) {
        let margm1 = '<div class="row d-flex"  style="color:#6f6f6f">'
        margm1 += '<a>Thanks for showing interest in Marg Software. Please select your inquiry type.</a>'
        margm1 += '</div><div class="row d-flex">'
        margm1 += '<a class="cbot-btn" href="https://www.margcompusoft.com/landingPages/billing_software.html?utm_source=Direct&utm_medium=homepage&utm_campaign=Free_Demo" target="_blank" style="color:#009900">Book Demo</a>'
        margm1 += '<a class="cbot-btn" href="https://margcompusoft.com/marg-price-list.html" target="_blank" style="color:#660000">Pricing💰</a>'
        margm1 += '</div><div class="row d-flex">'
        margm1 += '<button class="cbot-btn" id="mybttn" onclick="this.newUser()">What is Marg ERP?</button>'
        margm1 += '</div>'
        let msg1 = { name: "MargBot", message: margm1 };
        this.messages.push(msg1);

        this.updateChatText(chatbox);
        window.myvalue = window.myvalue+1
      } else {
        window.margq = window.margq+1
      }
        //window.margq = window.margq+1
      //}
      if(window.margq===1) {
        let margm1 = '<div class="row d-flex">'
        margm1 += '<a style="font-size:13px">MARG ERP 9+ is an on-premise ERP solution used by small, midsize and enterprise businesses. It offers different modules customized to the needs of retailers, distributors and manufacturers in a variety of industries.</a>'
        margm1 += '</div>'
        margm1 += '</div>'
        let msg1 = { name: "MargBot", message: margm1 };
        this.messages.push(msg1);

        let margm2 = '<div class="row d-flex">'
        margm2 += '<a> For more information, visit at : </a></div><div>'
        margm2 += '<a href="https://www.margerp.com" target="_blank">www.margerp.com</a>'
        margm2 += '</div>'
        let msg2 = { name: "MargBot", message: margm2 };
        this.messages.push(msg2);

        this.updateChatText(chatbox);
        window.margq = window.margq+1
      }
    }

    toggleState(chatbox) {
        this.state = !this.state;
        if(this.state) {
          chatbox.classList.add('chatbox--active')
          if(window.value===0) {
            window.value = window.value+1;
            let margm2 = "Happy to help you explore some interesting things! How about starting with one of the below ones? 👇"
            let msg2 = { name: "MargBot", message: margm2 };
            this.messages.push(msg2);
            let margm1 = '<div class="row d-flex">'
            margm1 += '<button class="cbot-btn" id="mybttn" onclick="this.newUser()">New User</button>'
            margm1 += '<button class="cbot-btn" id="mybttn" onclick="this.existing()">Existing</button>'
            margm1 += '</div>'
            let msg1 = { name: "MargBot", message: margm1 };
            this.messages.push(msg1);
            this.updateChatText(chatbox)
          }
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }


    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }
        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        //fetch('http://127.0.0.1:5000/predict', {
        fetch($SCRIPT_ROOT +'/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "MargBot", message: r.answer };
            this.messages.push(msg2);
            let msgU = r.urls;
            if(msgU) {
              let margm3 = '<div class="row d-flex">'
              margm3 += '<a href="https://www.google.com/" target="_blank">'+msgU+' </a>'
              margm3 += '</div>'
              let msg3 = { name: "MargBot", message: margm3 };
              this.messages.push(msg3);
            }
            let msgI = r.image;
            if(msgI) {
              let margm4 = '<div class="row d-flex">'
              margm4 += '<img src="static/images/'+msgI+'" />'
              margm4 += '</div>'
              let msg4 = { name: "MargBot", message: margm4 };
              this.messages.push(msg4);
            }

            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
      const dt = new Date();
      var hours = dt.getHours() > 12 ? dt.getHours() - 12 : dt.getHours();
      var am_pm = dt.getHours() >= 12 ? "PM" : "AM";
      var month = new Array();
      month[0] = "Jan.";
      month[1] = "Feb.";
      month[2] = "Mar.";
      month[3] = "Apr.";
      month[4] = "May";
      month[5] = "Jun.";
      month[6] = "Jul.";
      month[7] = "Aug.";
      month[8] = "Sep.";
      month[9] = "Oct.";
      month[10] = "Nov.";
      month[11] = "Dec.";
      //var dtd = (("0"+dt.getDate()).slice(-2)) +"."+ (("0"+(dt.getMonth()+1)).slice(-2)) +"."+ (dt.getFullYear()) +" "+ (("0"+dt.getHours()).slice(-2)) +":"+ (("0"+dt.getMinutes()).slice(-2))
      var dtd = (("0"+dt.getDate()).slice(-2)) +" "+ (month[dt.getMonth()]) +","+ (dt.getFullYear()) +", "+ (("0"+hours).slice(-2)) +":"+ (("0"+dt.getMinutes()).slice(-2))
      var html = '';
      this.messages.slice().reverse().forEach(function(item, index) {
        if (item.name === "MargBot") {
          //alert(item.message);
          html += '<div style="font-size:11px; color:#666666">' + dtd + ' '+am_pm +'</div>'
          html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
        } else {
          html += '<div style="display: inline-block;font-size:10px;color:#666666;text-align: right; width: 100%">' + dtd + ' '+am_pm + '</div>'
          html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
        }
      });
      //alert(html);
      const chatmessage = chatbox.querySelector('.chatbox__messages');
      chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();

$( chatbox ).ready(function() {
   $('#showMe').delay(100000).show(0);
});
