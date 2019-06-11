def HissingMicrophone(word)
  if word.include? "ss"
    return "hiss"
  else
    return "no hiss"
  end
end

def main()
  word = $stdin.read.strip
  puts HissingMicrophone(word)
end

main()
