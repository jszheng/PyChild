class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performLogicGate()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input("Enter	Pin	A input	for	gate " + self.get_label() + "-->")
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input("Enter	Pin	B input	for	gate " + self.get_label() + "-->")
        else:
            return self.pinB.getFrom().getOutput()

    def setNextpin(self, source):

        if self.pinA == None:
            self.pinA = source

        elif self.pinB == None:
            self.pinB = source

        else:
            raise RuntimeError('ERROR: NO EMPTY PIN!')




class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        return int(input("Enter	Pin	input for gate " + self.get_label() + "-->"))


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performLogicGate(self):

        a = self.getPinA()
        b = self.getPinB()

        if a==1 and b==1:
            return 1

        else:
            return 0


# g1 = AndGate('G1')
# print(g1.get_output())

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performLogicGate(self):

        a = self.getPinA()
        b = self.getPinB()

        if a ==0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performLogicGate(self):

        a = self.getPin()

        if a == 1:
            return 0

        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):

        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextpin(self)

    def getFromGate(self):
        return self.fromgate

    def getToGate(self):
        return self.togate










