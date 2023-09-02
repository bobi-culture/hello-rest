pipeline {
  agent any
  stages {
    stage('Hello') {
      steps {
        sh 'echo Hello'
      }
    }
    stage(cat READ.me") {
      when {
        branch "fix-*"
      }
      steps {
        sh ''' 
           cat READ.me
            ''' 
  }  
}
