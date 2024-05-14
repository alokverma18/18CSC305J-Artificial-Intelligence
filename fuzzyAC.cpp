#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class FuzzySet {
private:
    vector<double> values;

public:
    FuzzySet(vector<double> vals) : values(vals) {}

    double getValue(double input) {
        return values[static_cast<int>(round(input))];
    }
};

class Antecedent : public FuzzySet {
public:
    Antecedent(vector<double> vals) : FuzzySet(vals) {}
};

class Consequent : public FuzzySet {
public:
    Consequent(vector<double> vals) : FuzzySet(vals) {}
};

class Rule {
private:
    Antecedent *antecedent1;
    Antecedent *antecedent2;
    Consequent *consequent;

public:
    Rule(Antecedent *ant1, Antecedent *ant2, Consequent *cons) : antecedent1(ant1), antecedent2(ant2), consequent(cons) {}

    double evaluate(double input1, double input2) {
        return max(antecedent1->getValue(input1), antecedent2->getValue(input2));
    }

    Consequent* getConsequent() {
        return consequent;
    }
};

class ControlSystem {
private:
    vector<Rule*> rules;

public:
    ControlSystem(vector<Rule*> r) : rules(r) {}

    double computeOutput(double input1, double input2) {
        double maxVal = 0.0;
        for (Rule* rule : rules) {
            double val = rule->evaluate(input1, input2);
            maxVal = max(maxVal, val);
        }
        return maxVal;
    }
};

class ControlSystemSimulation {
private:
    ControlSystem *controlSystem;
    double input1;
    double input2;

public:
    ControlSystemSimulation(ControlSystem *cs, double in1, double in2) : controlSystem(cs), input1(in1), input2(in2) {}

    double compute() {
        return controlSystem->computeOutput(input1, input2);
    }
};

int main() {
    vector<double> room_condition_values = {1, 2, 3, 4, 5};
    vector<double> humidity_values = {1, 2, 3, 4, 5};
    vector<double> ac_temperature_values = {1, 2, 3, 4, 5};
    vector<double> room_condition_level_values = {1, 2, 3, 4, 5};
    vector<double> temperature_level_values = {1, 2, 3, 4, 5};

    Antecedent room_condition(room_condition_values);
    Antecedent humidity(humidity_values);
    Consequent ac_temperature(ac_temperature_values);
    Consequent room_condition_level(room_condition_level_values);
    Consequent temperature_level(temperature_level_values);

    Rule rule1(&room_condition, &humidity, &ac_temperature);
    Rule rule2(&room_condition, &humidity, &ac_temperature);
    // Define other rules similarly

    vector<Rule*> rules = {&rule1, &rule2 /* Add other rules here */};

    ControlSystem ac_ctrl(rules);

    double input_room_condition, input_humidity;
    cout << "Enter room condition (1-5): ";
    cin >> input_room_condition;
    cout << "Enter humidity (1-5): ";
    cin >> input_humidity;

    ControlSystemSimulation ac_temp_ctrl(&ac_ctrl, input_room_condition, input_humidity);

    double output = ac_temp_ctrl.compute();

    cout << "For room condition: " << input_room_condition << endl;
    cout << "and humidity: " << input_humidity << endl;
    cout << "AC Temperature: " << output << endl;

    if (output >= 3) {
        cout << "Room condition is high." << endl;
    } else {
        cout << "Room condition is low." << endl;
    }

    if (output >= 3) {
        cout << "Temperature is high." << endl;
    } else {
        cout << "Temperature is low." << endl;
    }

    return 0;
}