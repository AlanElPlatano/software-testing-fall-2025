# Checks some basic commit message style:
#   - The title (first line) is not longer than 50 characters (except "Merge" commits).
#   - The title and body have to be separated by newline.
#   - The description has minimum 5 characters.
#   - Each description line is not longer than 72 characters.

commitIssues = []

for commit in git.commits
  (subject, empty_line, *body) = commit.message.split("\n")

  # Solo validar longitud si no empieza con "Merge"
  unless subject.start_with?("Merge")
    commitIssues << "Commit title is too long: <#{subject}>" if subject.length > 50
  end

  commitIssues << "Commit title and body are not separated: <#{subject}>" if empty_line && empty_line.length > 0

  description_length = body.length > 0 ? body.first.length : 0
  commitIssues << "Please include a description for commit \"#{subject}\"" if (description_length < 5)

  for line in body
    commitIssues << "Commit text lines are too long: <#{subject}>" if line.length > 72
  end
end

for issue in commitIssues
  fail issue
end
