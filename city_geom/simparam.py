class SimParam(object):
    """
    SimParam
    Calculates simulation time parameters based on initial date
    and weather data time step, and simulation timestep

    properties
        dt            % Simulation time-step
        timeForcing   % Weather data time-step
        month         % Begin month
        day           % Begin day of the month
        days          % Number of days of simulation
        timePrint     % time-step for printing outputs
        timeDay       % number of timesteps in a design-day
        timeSim       % number of timesteps of the simulation
        timeMax       % total simulation time (s)
        nt            % total number of timesteps
        timeFinal     % final timestep of simulation
        timeInitial   % initial timestep of simulation
        secDay        % seconds of one day (s)
        hourDay       % hour of the day (0 - 23hr)
        inobis        % julian day at the end of each month
        julian        % julian day
    """

    def __init__(self,dt,timefor,M,DAY,days):
        self.dt = dt
        self.timeForcing = timefor #weather data timestep
        self.month = int(M)
        self.day = DAY
        self.days = days
        self.timePrint = timefor
        self.timeDay = 24*3600/timefor #how many times weather senses in a day
        self.timeSim = self.timeDay*days #how many steps in simulation
        self.timeMax = 24.*3600.*days
        self.nt = int(round(self.timeMax/self.dt+1)) #total number of timesteps
        self.inobis = [0,31,59,90,120,151,181,212,243,273,304,334]
        self.julian = self.inobis[self.month - 1] + DAY - 1
        #H1: (julian day * number of timesteps in a day) == sensor data index in epw
        H1 = int((self.inobis[self.month - 1] + DAY - 1) * self.timeDay)
        self.timeInitial = H1 + 8
        self.timeFinal = int(H1 + self.timeDay * self.days - 1 + 8)
        self.secDay = 0
        self.hourDay = 0

        #TODO: needs to be unit tested
        def UpdateDate(self):
            self.secDay = self.secDay + self.dt
            if self.secDay == 3600*24:
                self.day = self.day + 1
                self.julian = self.julian + 1
                self.secDay = 0
                for j in xrange(12):
                    if self.julian == self.inobis[j]:
                        self.month = self.month + 1
                        self.day = 1
            self.hourDay = floor(self.secDay/3600)       # 0 - 23hr

    def __repr__(self):
        return "SimParam: start={a}/{b}, num time steps={c},for days={d}.".format(
            a=self.month,
            b=self.day,
            c=self.timeSim,
            d=self.days
            )
