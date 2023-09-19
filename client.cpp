#include "client_generated.h"
#include <iostream>
#include <fstream>

using namespace Test;

int main(int argc, const char * argv[])
{

    if(argc != 2)
    {
        std::cout << "Usage : <executable name> <binary_file_path>" << std::endl;
        return 0;
    }

    flatbuffers::FlatBufferBuilder builder;

    auto person_name = builder.CreateString("Ram");

    auto person = CreatePerson(builder, person_name, 21, 76.5, Gender_Male);

    std::vector<std::string>vector_of_list_of_names{"Ram","Shayam","Raghuveer"};

    auto group_name = builder.CreateString("FightClub");

    auto group_names_list = builder.CreateVectorOfStrings(vector_of_list_of_names);

    auto group = CreateGroup(builder, group_name, 24.5, 66, group_names_list);

    auto client = CreateClient(builder,TypeOfClient_Person,person.Union());

    builder.Finish(client);

    const char* output_file_name = argv[1];

    std::ofstream output_file(output_file_name, std::ios::binary);

    if (!output_file) {
        std::cerr << "Failed to open output file: " << output_file_name << std::endl;
        return 1;
    }

    uint8_t *buf = builder.GetBufferPointer();

    int size = builder.GetSize();

    output_file.write(reinterpret_cast<const char*>(buf), size);

    output_file.close();

    std::cout << "FlatBuffers data saved to '" << output_file_name << "'." << std::endl;

    return 0;

}