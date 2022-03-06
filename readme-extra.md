# Step1: install unixodbc 
brew install unixodbc

# Step2: install Microsoft ODBC Driver for SQL Server on MacOS

brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install msodbcsql mssql-tools

# Step3：verify odbcinst configuration path is correct

odbcinst -j

sudo ln -s /usr/local/etc/odbcinst.ini /etc/odbcinst.ini
sudo ln -s /usr/local/etc/odbc.ini /etc/odbc.ini


pip install knox

