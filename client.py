import Test.Client
import Test.Gender
import Test.Group
import Test.Person
import Test.TypeOfClient
import sys
import os

import flatbuffers

def main():

    if(len(sys.argv) != 2):
        print("Usage : python3 client.py <encoded_binary_file_path>")
        return

    if(not os.path.isfile(sys.argv[1])):
        print("Binary file not found")
        return

    input_file_name = sys.argv[1]

    with open(input_file_name, "rb") as input_file:
            binary_data = input_file.read()

    buf = bytearray(binary_data)

    client=Test.Client.Client.GetRootAs(buf,0)

    if client.ClientTypeType() == Test.TypeOfClient.TypeOfClient().Person:

        person = Test.Person.Person()

        person.Init(client.ClientType().Bytes, client.ClientType().Pos)

        assert person.Name().decode() == "Ram"
        assert person.Age() == 21
        assert round(person.Weight()) == 76
        assert person.Gender() == Test.Gender.Gender().Male
        print(person.Name().decode(),person.Age(),person.Weight(),person.Gender(),end=" ")

    else:
        
        group = Test.Group.Group()
        group.Init(client.ClientType().Bytes, client.ClientType().Pos)

        assert group.GrpName().decode() == "FightClub"
        assert round(group.AvgAge()) == 24
        assert round(group.AvgWeight()) == 66
        expected_list_names = ["Ram","Shayam","Raghuveer"]

        print_list_names = []
        for i in range(group.ListNamesLength()):
            assert group.ListNames(i).decode() == expected_list_names[i]
            print_list_names.append(group.ListNames(i).decode())
    
        print_group_list_names = ' '.join(print_list_names)

        print(group.GrpName().decode(),group.AvgAge(),group.AvgWeight(),print_group_list_names,end=" ")

    print('The FlatBuffer was successfully decoded!')    

if __name__ == '__main__':
    main()