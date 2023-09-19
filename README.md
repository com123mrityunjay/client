# client
1. First we should have flatc already built so that we can use it to generate the code from the schema.
To compile use the below command
```sh
  C++ : /path/to/flatc --cpp client.fbs
  Python : /path/to/flatc --python client.fbs
  ```

2. Then use the below command to generate the fb_encoder executable and run that to produce the bin file

```sh
   g++ -o fb_encoder client.cpp -I/Users/mrityunjayjha/client/flatbuffers/include -std=c++11
   ./fb_encoder <bin_file_path>
   ```

3. Run the python file using the command below to decode the text
```sh
   python3 client.py <bin_file_path>
   ```

Please Note : If you want to print Person or Group name you need to change accordingly in 30th line in client.cpp as this:
  Person
```cpp
   auto client = CreateClient(builder,TypeOfClient_Person,person.Union());
   ```
  Group
 ```cpp
   auto client = CreateClient(builder,TypeOfClient_Group,group.Union());
   ```
