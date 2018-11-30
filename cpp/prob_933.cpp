class RecentCounter {
public:
    int TIME_WINDOW = 3000;
    vector <int> recent_pings_queue;
    
    int ping(int t) {
        int ping_time_diff = t - this->TIME_WINDOW;
        vector <int>::iterator it_begin;
        
        it_begin = this->recent_pings_queue.begin();
        
        this->recent_pings_queue.insert(it_begin, t);
        while(this->recent_pings_queue.back() < ping_time_diff) {
            this->recent_pings_queue.pop_back();
        }
        return this->recent_pings_queue.size();
    }
};