function scoreChecker(score) {
  if (score < 150) {
    window.alert('Youre doing pretty bad..');
  } else if (250 >= score >= 150) {
    window.alert ('Not bad');
  } else if (350 >= score >= 250) {
    window.alert ('Keep up the good work!');
  } else if (450 >= score >= 350) {
    window.alert ('Great job!');
  } else if (score > 450) {
    window.alert ('Youre amazing!!');
  };
}
