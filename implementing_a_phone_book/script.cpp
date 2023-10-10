#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

class Person {
public:
    Person(const std::string& firstName, const std::string& lastName, const std::string& phoneNumber)
        : firstName(firstName), lastName(lastName), phoneNumber(phoneNumber) {}

    void display() const {
        std::cout << firstName << " " << lastName << ": " << phoneNumber << std::endl;
    }

    const std::string& getFirstName() const { return firstName; }
    const std::string& getLastName() const { return lastName; }
    const std::string& getPhoneNumber() const { return phoneNumber; }

private:
    std::string firstName;
    std::string lastName;
    std::string phoneNumber;
};

class PhoneBook {
public:
    void addPerson(const Person& person) {
        phoneBook.push_back(person);
        std::sort(phoneBook.begin(), phoneBook.end(), [](const Person& a, const Person& b) {
            return (a.getLastName() == b.getLastName()) ? (a.getFirstName() < b.getFirstName()) : (a.getLastName() < b.getLastName());
        });
    }

    void deletePerson(const std::string& firstName, const std::string& lastName) {
        auto it = std::remove_if(phoneBook.begin(), phoneBook.end(), [&](const Person& person) {
            return (person.getFirstName() == firstName) && (person.getLastName() == lastName);
        });
        phoneBook.erase(it, phoneBook.end());
    }

    const Person* findPerson(const std::string& firstName, const std::string& lastName) const {
        for (const auto& person : phoneBook) {
            if (person.getFirstName() == firstName && person.getLastName() == lastName) {
                return &person;
            }
        }
        return nullptr;
    }

    void changePhoneNumber(const std::string& firstName, const std::string& lastName, const std::string& newPhoneNumber) {
        for (auto& person : phoneBook) {
            if (person.getFirstName() == firstName && person.getLastName() == lastName) {
                person = Person(firstName, lastName, newPhoneNumber);
                return;
            }
        }
    }

    void display() const {
        for (const auto& person : phoneBook) {
            person.display();
        }
    }

    void saveToFile(const std::string& filename) const {
        std::ofstream file(filename);
        if (!file) {
            std::cerr << "Error opening file for writing." << std::endl;
            return;
        }

        for (const auto& person : phoneBook) {
            file << person.getFirstName() << "," << person.getLastName() << "," << person.getPhoneNumber() << "\n";
        }

        std::cout << "Phone book saved to file." << std::endl;
    }

    void loadFromFile(const std::string& filename) {
        phoneBook.clear();
        std::ifstream file(filename);
        if (!file) {
            std::cerr << "Error opening file for reading." << std::endl;
            return;
        }

        std::string line;
        while (std::getline(file, line)) {
            size_t pos1 = line.find(",");
            size_t pos2 = line.rfind(",");
            if (pos1 != std::string::npos && pos2 != std::string::npos && pos1 < pos2) {
                std::string firstName = line.substr(0, pos1);
                std::string lastName = line.substr(pos1 + 1, pos2 - pos1 - 1);
                std::string phoneNumber = line.substr(pos2 + 1);
                addPerson(Person(firstName, lastName, phoneNumber));
            }
        }

        std::cout << "Phone book loaded from file." << std::endl;
    }

private:
    std::vector<Person> phoneBook;
};

class UserInterface {
public:
    void run() {
        PhoneBook phoneBook;
        std::string filename = "phonebook.txt";  // Default filename

        while (true) {
            std::cout << "\nPhone Book Application" << std::endl;
            std::cout << "1. Add" << std::endl;
            std::cout << "2. Delete" << std::endl;
            std::cout << "3. Find" << std::endl;
            std::cout << "4. Change" << std::endl;
            std::cout << "5. Display" << std::endl;
            std::cout << "6. Save to File" << std::endl;
            std::cout << "7. Load from File" << std::endl;
            std::cout << "8. Quit" << std::endl;

            int choice;
            std::cout << "Enter your choice: ";
            std::cin >> choice;
            std::cin.ignore();  // Consume newline character

            switch (choice) {
                case 1: {
                    std::string firstName, lastName, phoneNumber;
                    std::cout << "Enter first name: ";
                    std::getline(std::cin, firstName);
                    std::cout << "Enter last name: ";
                    std::getline(std::cin, lastName);
                    std::cout << "Enter phone number: ";
                    std::getline(std::cin, phoneNumber);
                    phoneBook.addPerson(Person(firstName, lastName, phoneNumber));
                    break;
                }
                case 2: {
                    std::string firstName, lastName;
                    std::cout << "Enter first name: ";
                    std::getline(std::cin, firstName);
                    std::cout << "Enter last name: ";
                    std::getline(std::cin, lastName);
                    phoneBook.deletePerson(firstName, lastName);
                    break;
                }
                case 3: {
                    std::string firstName, lastName;
                    std::cout << "Enter first name: ";
                    std::getline(std::cin, firstName);
                    std::cout << "Enter last name: ";
                    std::getline(std::cin, lastName);
                    const Person* person = phoneBook.findPerson(firstName, lastName);
                    if (person) {
                        std::cout << "Phone number: " << person->getPhoneNumber() << std::endl;
                    } else {
                        std::cout << firstName << " " << lastName << " not found in the phone book." << std::endl;
                    }
                    break;
                }
                case 4: {
                    std::string firstName, lastName, newPhoneNumber;
                    std::cout << "Enter first name: ";
                    std::getline(std::cin, firstName);
                    std::cout << "Enter last name: ";
                    std::getline(std::cin, lastName);
                    std::cout << "Enter new phone number: ";
                    std::getline(std::cin, newPhoneNumber);
                    phoneBook.changePhoneNumber(firstName, lastName, newPhoneNumber);
                    break;
                }
                case 5:
                    std::cout << "Phone Book:" << std::endl;
                    phoneBook.display();
                    break;
                case 6: {
                    std::cout << "Enter filename to save: ";
                    std::getline(std::cin, filename);
                    phoneBook.saveToFile(filename);
                    break;
                }
                case 7: {
                    std::cout << "Enter filename to load: ";
                    std::getline(std::cin, filename);
                    phoneBook.loadFromFile(filename);
                    break;
                }
                case 8:
                    std::cout << "Exiting the application." << std::endl;
                    return;
                default:
                    std::cout << "Invalid choice. Please try again." << std::endl;
            }
        }
    }
};

int main() {
    UserInterface ui;
    ui.run();
    return 0;
}
